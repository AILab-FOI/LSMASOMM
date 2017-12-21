#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spade
import time
import random
import re
import csv
from datetime import datetime
# import xmlrpclib
import networkx as nx
from pynteractive import *

import sys
import os

sys.path.append('..' + os.sep + 'trunk')
sys.path.append('..')

visualise = False
charting = False

# how many Factory agents will be run? 0 uses manually defined vertices and edges
numOfFactories = 60
# how many Order agents will be run?
numOfOrders = 1000
# number of the available services
numOfServices = 20
# minimum starting Money for an Order
OrderMoneyStartMin = 250
# maximum starting Money of an Order
OrderMoneyStartMax = 500
# starting Money for a Factory
FactoryMoneyStart = 10
# prices of each of the available Services
priceOfService = [15, 40, 68, 25, 80, 75, 92, 14, 47, 93, 79, 84, 18, 64, 73, 81, 35, 27, 19, 39]# , 31, 65, 62, 22, 66, 44, 23, 55, 67, 99, 58, 11, 50, 76, 13, 51, 56, 32, 96, 12]
# time needed for each of the Services
timesOfService = [13, 4, 12, 9, 6, 10, 13, 3, 6, 13, 15, 7, 6, 11, 10, 15, 4, 2, 6, 6]# , 15, 7, 13, 15, 10, 1, 3, 1, 12, 6, 11]# , 12, 14, 12, 14, 11, 2, 5, 10, 15]

# throw error if not all services are given a base price
if not len(priceOfService) == numOfServices:
    print("ERROR: Not all services are priced! Edit service prices.")
    raise SystemExit(0)
    # raise ValueError("Not all services are priced! Edit service prices.")
# number of recipe pieces for each Order agent
numOfRecipePieces = 4
# max number of services provided by each Factory
numOfServicesPerFactory = 2

# Graph initialization
if visualise:
    N = Graph(directed=False)
    N.view()
    N.clear()
G = nx.Graph()

# show graph in browser
if charting:
    C = Chart()
    C.view()

# initialize dictionary of everything happening
network = {
    'nodes': {
        'factories': {},
        'orders': {},
        'recipePcs': {}
        },
    'edges': {},
    'errors': []
    }

def say(text):
    # print (text)
    pass

class AgentOrder(spade.Agent.Agent):
    """Class of Order agents waiting to be worked on by a Factory agent"""

    class SearchForFactories(spade.Behaviour.OneShotBehaviour):
        """Search for factories and their services"""
        def onStart(self):
            if not self.myAgent.startProductionFlag and not self.myAgent.finishProductionFlag:
                self.myAgent.possibleFactories = {}

                s = spade.DF.Service(
                    name="Service{}".format(
                        self.myAgent.recipe[-1]['value']))
                search = self.myAgent.searchService(s)

                self.myAgent.possibleFactories = {x.getOwner().getName(): x.getName() for x in search}
                if self.myAgent.triedFactories:
                    try:
                        for f in self.myAgent.triedFactories:
                            del self.myAgent.possibleFactories[f]
                    except Exception as e:
                        print e

                    say("{}: Already tried {}".format(
                        self.myAgent.getName(),
                        self.myAgent.triedFactories))

                say("{}: Considered factories are {} ({}, {})".format(
                       self.myAgent.getName(),
                       self.myAgent.possibleFactories,
                       self.myAgent.finishProductionFlag,
                       self.myAgent.startProductionFlag))

            if self.myAgent.finishProductionFlag:
                self._exitcode = self.myAgent.transition2To4
            elif self.myAgent.startProductionFlag:
                self._exitcode = self.myAgent.transition2To5
            else:
                self._exitcode = self.myAgent.transition2To3

        def _process(self):
            pass

    class CheckFactoryAvailability(spade.Behaviour.OneShotBehaviour):
        """Check if the desired Factory is free"""
        def onStart(self):
            say("{}: Checking factory availability.".format(
                self.myAgent.getName()))

            if not self.myAgent.possibleFactories:
                if visualise:
                    N.log("{}: Impossible to produce RP {}. Terminating production.".format(
                          self.myAgent.getName(),
                          self.myAgent.recipe[-1]['value']))
                    N.updateNode(
                        self.myAgent.node[0],
                        color='black')
                say("{}: Impossible to produce RP {}. Terminating production.".format(
                    self.myAgent.getName(),
                    self.myAgent.recipe[-1]['value']))

                print("{}: Cannot produce.".format(
                    self.myAgent.getName()))

                self.myAgent._kill()

            else:
                say(self.myAgent.chosenFactory)
                if not self.myAgent.chosenFactory:
                    self.myAgent.chosenFactory = random.choice(self.myAgent.possibleFactories.keys())
                    factory = self.myAgent.chosenFactory

                # choose the closest of the desirable factories
                else:
                    try:
                        localGroup = list(nx.node_connected_component(G, int(self.myAgent.chosenFactory.split("@")[0])))
                        say(localGroup)
                        factories = self.myAgent.possibleFactories.keys()
                        for f in factories:
                            if int(f.split("@")[0]) not in localGroup:
                                del self.myAgent.possibleFactories[f]
                        say(self.myAgent.possibleFactories)

                        if not self.myAgent.possibleFactories:
                            if visualise:
                                N.log("%s: Impossible to produce RP %d. Terminating production." % (
                                    self.myAgent.getName(), self.myAgent.recipe[-1]['value']))
                                N.updateNode(
                                    self.myAgent.node[0],
                                    color='black')
                            say("{}: Impossible to produce RP {}. Terminating production.".format(
                                self.myAgent.getName(),
                                self.myAgent.recipe[-1]['value']))
                            print("{}: Cannot produce.".format(
                                self.myAgent.getName()))

                            self.myAgent._kill()
                    except Exception as e:
                        print e

                    paths = {f: nx.shortest_path_length(G, int(self.myAgent.chosenFactory.split("@")[0]), weight='weight')[int(f.split("@")[0])] for f in self.myAgent.possibleFactories}
                    say("{}: Considered paths from {} are {}.".format(
                        self.myAgent.getName(),
                        self.myAgent.chosenFactory,
                        paths))
                    shortest = max(paths.values())
                    for f in paths.keys():
                        if f == self.myAgent.chosenFactory:
                            factory = f
                            break

                        elif paths[f] < shortest:
                            shortest = paths[f]
                            factory = f

                        elif paths[f] == shortest:
                            factory = f

                    self.myAgent.chosenFactory = factory

                say("{}: Chosen factory {}.".format(
                    self.myAgent.getName(),
                    self.myAgent.chosenFactory))

                self.myAgent.chosenFactoryAID = spade.AID.aid(
                    name=factory,
                    addresses=["xmpp://%s" % factory])
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("propose")
                msg.addReceiver(self.myAgent.chosenFactoryAID)
                msg.setContent("{}".format(self.myAgent.possibleFactories[factory][7:]))

                tmplt = spade.Behaviour.ACLTemplate()
                tmplt.setSender(self.myAgent.chosenFactoryAID)
                t = spade.Behaviour.MessageTemplate(tmplt)

                self.myAgent.addBehaviour(self.myAgent.WaitForFactoryAnswer(), t)

                self.myAgent.send(msg)
        def _process(self):
            pass

    class WaitForFactoryAnswer(spade.Behaviour.EventBehaviour):
        """docstring for WaitForFactoryAnswer"""
        def onStart(self):
            self.msg = None

            self.msg = self._receive()

            if self.msg:
                if "reject" in self.msg.getPerformative():
                    self.myAgent.startProductionFlag = False
                    self.myAgent.triedFactories.append(
                        self.msg.getSender().getName())
                    self.myAgent.chosenFactory = self.myAgent.lastFactory
                    time.sleep(0.5)

                elif "accept" in self.msg.getPerformative():
                    if self.myAgent.moneyOwned > int(self.msg.getContent()):
                        self.myAgent.startProductionFlag = True
                        self.myAgent.lastFactory = self.msg.getSender().getName()
                    else:
                        self.myAgent.startProductionFlag = False
                        print("{}: Need more money!".format(
                            self.myAgent.getName()))
                        if visualise:
                            N.log("{}: Impossible to produce RP {}. Terminating production.".format(
                                  self.myAgent.getName(),
                                  self.myAgent.recipe[-1]['value']))
                            N.updateNode(
                                self.myAgent.node[0],
                                color='black')

                        msg = spade.ACLMessage.ACLMessage()
                        msg.setPerformative("propose")
                        msg.addReceiver(self.msg.getSender())
                        msg.setContent("decline")
                        self.myAgent.send(msg)

                        self.myAgent._kill()
                    time.sleep(0.2)

                elif "Produced" in self.msg.getContent():
                    if len(self.myAgent.recipe):
                        del self.myAgent.recipe[-1]
                    self.myAgent.startProductionFlag = False
                    if not len(self.myAgent.recipe):
                        self.myAgent.finishProductionFlag = True
                    self.myAgent.triedFactories = []
                    time.sleep(0.3)

            self.myAgent.removeBehaviour(self.myAgent.behav)
            if not self.myAgent.hasBehaviour(self.myAgent.behav):
                self.myAgent.setFSM()

        def _process(self):
            pass

    class StartProduction(spade.Behaviour.OneShotBehaviour):
        """deads"""
        global priceOfService

        def onStart(self):
            if len(self.myAgent.recipe):
                if visualise:
                    recipePart = self.myAgent.recipe[-1]['node']
                else:
                    recipePart = self.myAgent.recipe[-1]['value']

                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("request")
                msg.addReceiver(self.myAgent.chosenFactoryAID)
                msg.setContent(recipePart)
                msg.setOntology("recipeParts")
                self.myAgent.send(msg)

                if visualise:
                    self.myAgent.moneyOwned -= priceOfService[recipePart[1]]
                else:
                    self.myAgent.moneyOwned -= priceOfService[recipePart]

                self.myAgent.startProductionFlag = False
            else:
                pass

            tmplt = spade.Behaviour.ACLTemplate()
            tmplt.setSender(self.myAgent.chosenFactoryAID)
            t = spade.Behaviour.MessageTemplate(tmplt)

            if not self.myAgent.hasBehaviour(self.myAgent.WaitForFactoryAnswer):
                self.myAgent.addBehaviour(
                    self.myAgent.WaitForFactoryAnswer(), t)
        def _process(self):
            pass

    class FinishProduction(spade.Behaviour.OneShotBehaviour):
        """Finish production"""
        def onStart(self):
            if visualise:
                N.log("%s: It is done." % self.myAgent.getName())
                N.updateNode(
                    self.myAgent.node[0],
                    color='green'
                    )
            print("{}: Done!".format(self.myAgent.getName()))
            self.myAgent._kill()

        def _process(self):
            pass

    def _setup(self):
        global numOfServices

        print("{}: Started!".format(self.getName()))
        if visualise:
            self.node = N.addNode(
                self.agentID,
                color='yellow',
                shape='dot')
            network['nodes']['orders'][self]['node'] = self.node

            self.previous_recipePiece = None
        self.chosenFactory = None
        self.startProductionFlag = False
        self.finishProductionFlag = False
        self.recipe = []
        self.triedFactories = []
        self.lastFactory = None

        # recipe elements definition
        for y in range(0, numOfRecipePieces):
            x = random.randint(1, numOfServices)
            self.recipe.append({'value': x})
            if visualise:
                recipePiece = N.addNode(
                    color='silver',
                    shape='circle',
                    label=str(x))
                self.recipe[y]['node'] = recipePiece

                network['nodes']['recipePcs'][recipePiece[0]] = {
                    'value': x, 'order': self.node[0]}

                if self.previous_recipePiece is None:
                    edge = N.addEdge(recipePiece[0], self.node[0])
                    network['edges'][edge[0]] = [recipePiece[0], self.node[0]]
                else:
                    edge = N.addEdge(
                        recipePiece[0],
                        self.previous_recipePiece[0]
                        )
                    network['edges'][edge[0]] = [recipePiece[0], self.node[0]]
                self.previous_recipePiece = recipePiece

        network['nodes']['orders'][self]['recipe'] = self.recipe

        self.setFSM()

    def setFSM(self):
        # FSM definition
        self.codeState2 = 2
        self.codeState3 = 3
        self.codeState4 = 4
        self.codeState5 = 5

        self.transitionRecursive = 0
        self.transition2To5 = 25
        self.transition2To4 = 24
        self.transition2To3 = 23

        self.behav = spade.Behaviour.FSMBehaviour()
        self.behav.registerFirstState(
            self.SearchForFactories(),          self.codeState2)
        self.behav.registerState(
            self.CheckFactoryAvailability(),    self.codeState3)
        self.behav.registerState(
            self.StartProduction(),             self.codeState5)
        self.behav.registerState(
            self.FinishProduction(),            self.codeState4)

        self.behav.registerTransition(
            self.codeState2,
            self.codeState3,
            self.transition2To3)
        self.behav.registerTransition(
            self.codeState2,
            self.codeState5,
            self.transition2To5)
        self.behav.registerTransition(
            self.codeState2,
            self.codeState4,
            self.transition2To4)

        self.addBehaviour(self.behav, None)


class AgentFactory(spade.Agent.Agent):
    global priceOfService
    global timesOfService
    global FactoryColours
    """Class of Factory agents"""
    class AnswerQuery(spade.Behaviour.EventBehaviour):
        # global priceOfService

        def onStart(self):
            msg = self._receive()

            receiver = msg.getSender()
            # if content is service no, save it,
            # otherwise do nothing with content, it is a 'decline' message
            try:
                service = int(msg.getContent())
            except Exception as e:
                print e

            if msg.getContent() == 'decline':
                self.myAgent.occupied = False
                self.kill()
            else:
                msg = spade.ACLMessage.ACLMessage()
                msg.addReceiver(receiver)

                if self.myAgent.occupied:
                    msg.setPerformative("reject-proposal")
                    msg.setContent("No room. Wait.")
                    say("{}: Can't produce for you {}".format(
                        self.myAgent.getName(),
                        receiver.getName()))
                else:
                    msg.setPerformative("accept-proposal")
                    msg.setContent(priceOfService[service - 1] * self.myAgent.priceWeight)
                    self.myAgent.occupied = True
                    say("{}: Can produce for you {}".format(
                        self.myAgent.getName(),
                        receiver.getName()))
                self.myAgent.send(msg)

    class AnswerTakeoverNegotiation(spade.Behaviour.EventBehaviour):
        def onStart(self):
            msg = self._receive()

            receiver = msg.getSender()
            msgContent = msg.getContent()

            if msg.getPerformative() == "propose-takeover":
                msg = spade.ACLMessage.ACLMessage()
                msg.addReceiver(receiver)
                msg.setPerformative("request-value")
                msg.setOntology("takeovers")
                msg.setContent(self.myAgent.moneyOwned)
                say("{}: Will sell myself for {} money".format(
                    self.myAgent.getName(),
                    self.myAgent.moneyOwned))
                self.myAgent.send(msg)

            elif msg.getPerformative() == "request-value":
                say("{0}: # # # # # Takeover? {0}({1}) vs {2}({3})".format(
                    self.myAgent.getName(),
                    self.myAgent.moneyOwned,
                    receiver.getName(),
                    msgContent))
                if self.myAgent.moneyOwned > int(msgContent):
                    msg = spade.ACLMessage.ACLMessage()
                    msg.addReceiver(receiver)
                    msg.setPerformative("accept-value")
                    msg.setOntology("takeovers")
                    msg.setContent("All your base are belong to us.")
                    self.myAgent.moneyOwned -= int(msgContent)
                    self.myAgent.myFactories.append(receiver.getName())
                    say("{}: # # # # # # Takeover!".format(
                        self.myAgent.getName()))
                else:
                    msg = spade.ACLMessage.ACLMessage()
                    msg.addReceiver(receiver)
                    msg.setPerformative("decline-value")
                    msg.setOntology("takeovers")
                    msg.setContent("No deal.")
                    say("{}: # # # # # # NO takeover!".format(
                        self.myAgent.getName()))
                self.myAgent.send(msg)

            elif msg.getPerformative() == "accept-value":
                msg = spade.ACLMessage.ACLMessage()
                msg.addReceiver(receiver)
                msg.setPerformative("accept-takeover")
                msg.setOntology("takeovers")
                msg.setContent("I've only ever served you my lord.")
                self.myAgent.send(msg)

                for f in self.myAgent.myFactories:
                    myF = spade.AID.aid(
                        name=f,
                        addresses=["xmpp://{}".format(f)])
                    msg = spade.ACLMessage.ACLMessage()
                    msg.addReceiver(myF)
                    msg.setPerformative("new-master")
                    msg.setOntology("takeovers")
                    msg.setContent(receiver.getName())
                    self.myAgent.send(msg)

                aad = spade.AMS.AmsAgentDescription()
                aad.ownership = receiver.getName()
                self.myAgent.modifyAgent(aad)

                # update node colour only, to visualise takeover
                if visualise:
                    N.updateNode(
                        self.myAgent.node[0],
                        color=FactoryColours[receiver.getName()],
                        title="{} ({}) {}".format(self.myAgent.getName(), receiver.getName(), self.myAgent.offeredServices),
                        label="{} ({} BTC)".format(
                            self.myAgent.getName().split("@")[0],
                            self.myAgent.moneyOwned))
                G.node[int(self.myAgent.name)]['ownership'] = receiver.getName().split("@")[0]

            elif msg.getPerformative() == "decline-value":
                msg = spade.ACLMessage.ACLMessage()
                msg.addReceiver(receiver)
                msg.setPerformative("decline-takeover")
                msg.setOntology("takeovers")
                msg.setContent("No deal.")
                self.myAgent.send(msg)

            elif msg.getPerformative() == "new-master":
                aad = spade.AMS.AmsAgentDescription()
                aad.ownership = msgContent
                self.myAgent.modifyAgent(aad)
                # update node colour only, to visualise takeover
                if visualise:
                    N.updateNode(
                        self.myAgent.node[0],
                        color=FactoryColours[receiver.getName()],
                        title="{} ({})".format(self.myAgent.getName(), receiver.getName()),
                        label="{} ({} BTC)".format(
                            self.myAgent.getName().split("@")[0],
                            self.myAgent.moneyOwned))
                G.node[int(self.myAgent.name)]['money'] = self.myAgent.moneyOwned
                G.node[int(self.myAgent.name)]['ownership'] = receiver.getName().split("@")[0]

    class TakeMoney(spade.Behaviour.EventBehaviour):
        def onStart(self):
            msg = self._receive()

            receiver = msg.getSender()
            msgContent = msg.getContent()

            if msg.getPerformative() == "inform":
                say("{}: Received {} money from {}.".format(
                    self.myAgent.getName(),
                    msgContent,
                    receiver.getName()))

                aad = spade.AMS.AmsAgentDescription()
                aad.setAID(spade.AID.aid(name=self.myAgent.getName()))
                res = self.myAgent.searchAgent(aad)

                if res[0].ownership == self.myAgent.getName():
                    self.myAgent.moneyOwned += int(msgContent)
                else:
                    receiver = spade.AID.aid(
                        name=res[0].ownership,
                        addresses=["xmpp://{}".format(res[0].ownership)])
                    msg = spade.ACLMessage.ACLMessage()
                    msg.setPerformative("inform")
                    msg.addReceiver(receiver)
                    msg.setOntology("money")
                    msg.setContent(int(msgContent))
                    say("{}: Sending {} money to {}".format(
                        self.myAgent.getName(),
                        int(msgContent),
                        res[0].ownership))
                    self.myAgent.send(msg)

                # update node size only
                if visualise:
                    N.updateNode(
                        self.myAgent.node[0],
                        label="{} ({} BTC)".format(
                            self.myAgent.getName().split("@")[0],
                            self.myAgent.moneyOwned))

                G.node[int(self.myAgent.name)]['money'] = self.myAgent.moneyOwned

    class ProvideData(spade.Behaviour.EventBehaviour):
        def onStart(self):
            msg = self._receive()

            receiver = msg.getSender()

            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform-value")
            msg.addReceiver(receiver)
            msg.setOntology("chart")
            msg.setContent(self.myAgent.moneyOwned)
            self.myAgent.send(msg)

    class Terminate(spade.Behaviour.EventBehaviour):
        def onStart(self):
            msg = self._receive()

            self.myAgent._kill()

    class Produce(spade.Behaviour.EventBehaviour):
        # global priceOfService
        def onStart(self):
            # self.server = xmlrpclib.ServerProxy('http://127.0.0.1:20738/RPC2')
            # self.G = self.server.ubigraph

            msg = self._receive()
            receiver = msg.getSender()

            if visualise:
                recipePart = eval(msg.getContent())
            else:
                recipePart = int(msg.getContent())

            try:
                if visualise:
                    edge = N.addEdge(
                        int(recipePart[0]),
                        self.myAgent.node[0]
                        )
                    N.updateNode(
                        self.myAgent.node[0],
                        shape='circle',
                        radius=2)

            except Exception, e:
                say("{}: Problem with {} for {}".format(
                    self.myAgent.getName(),
                    int(recipePart[0]),
                    msg.getSender().getName()))
                if visualise:
                    N.updateNode(int(recipePart[0]), color='#0000FF')
                # self.G.set_vertex_attribute(recipePart, 'color', '#0000FF')
                network['errors'].append(e)
                print e

            if visualise:
                time.sleep(timesOfService[int(recipePart[1])-1])
            else:
                time.sleep(timesOfService[recipePart-1])

            msg = spade.ACLMessage.ACLMessage()
            msg.addReceiver(receiver)

            msg.setPerformative("inform")
            msg.setContent("{}: Produced order part for {}".format(
                self.myAgent.getName(),
                receiver.getName()
                ))
            say("{}: Produced part for {}".format(
                self.myAgent.getName(),
                receiver.getName()))

            self.myAgent.send(msg)

            aad = spade.AMS.AmsAgentDescription()
            aad.setAID(spade.AID.aid(name=self.myAgent.getName()))
            res = self.myAgent.searchAgent(aad)

            res = [r for r in res if r.name.getName() == self.myAgent.getName()]

            if res[0].ownership == self.myAgent.getName():
                if visualise:
                    self.myAgent.moneyOwned += priceOfService[int(recipePart[1]) - 1]
                else:
                    self.myAgent.moneyOwned += priceOfService[recipePart - 1]

            else:
                receiver = spade.AID.aid(
                    name=res[0].ownership,
                    addresses=["xmpp://{}".format(res[0].ownership)])
                msg = spade.ACLMessage.ACLMessage()
                msg.setPerformative("inform")
                msg.addReceiver(receiver)
                msg.setOntology("money")
                if visualise:
                    msg.setContent(priceOfService[int(recipePart[1]) - 1])
                else:
                    msg.setContent(priceOfService[recipePart - 1])
                # say("{}: Sending {} money to {}".format(
                #     self.myAgent.getName(),
                #     priceOfService[int(recipePart[1]) - 1],
                #     res[0].ownership))
                self.myAgent.send(msg)

            self.myAgent.productionVolume += 1

            if visualise:
                N.updateNode(
                    self.myAgent.node[0],
                    shape='square',
                    color=FactoryColours[res[0].ownership],
                    radius=30,
                    label="{} ({} BTC)".format(
                        self.myAgent.getName().split("@")[0],
                        self.myAgent.moneyOwned))
            G.node[int(self.myAgent.name)]['money'] = self.myAgent.moneyOwned
            G.node[int(self.myAgent.name)]['productionVolume'] = self.myAgent.productionVolume

            # every Xth successfull production, check for possible takeovers
            # if F is not already owned by someone
            # if (self.myAgent.moneyOwned % 100 < 10 and res[0].ownership == self.myAgent.getName()):
            self.myAgent.occupied = False
            if (self.myAgent.productionVolume % 10 == 0 and res[0].ownership == self.myAgent.getName()):
                b = self.myAgent.CheckTakeovers()
                self.myAgent.addBehaviour(b, None)

    class CheckTakeovers(spade.Behaviour.OneShotBehaviour):
        """Check which Factory agent provide services not equal to this Factory."""
        def onStart(self):
            self.myAgent.possibleTakeovers = {}

            # for every available Service other than those offered by the Factory
            # if F is a Diversifier (aiming to overtake F's offering diverse services)
            if self.myAgent.factoryType == "Diversifier":
                services = [
                    x for x in xrange(1, numOfServices + 1)
                    if x not in self.myAgent.offeredServices]
            # for every available Service already offered by the Factory
            # if F is a Monopolist (aiming to overtake F's offering the same services)
            elif self.myAgent.factoryType == "Monopolist":
                services = self.myAgent.offeredServices

            for service in services:
                # setup search filter
                s = spade.DF.Service(
                    name="Service{}".format(service))
                res = self.myAgent.searchService(s)

                # write services and service providers in form:
                # {serviceNo: [serviceProviders]}
                self.myAgent.possibleTakeovers[service] = [
                    s.getOwner().getName() for s in res]

            say("{}: {}".format(
                self.myAgent.getName(),
                self.myAgent.possibleTakeovers))

            # for all the factories that provide the most provided service
            aad = spade.AMS.AmsAgentDescription()
            res = self.myAgent.searchAgent(aad)

            # freeFactories are owned by themselves and are not orders
            freeFactories = [f.name.getName() for f in res if (f.name.getName() == f.ownership and not f.name.getName()[:5] in ['order', 'chart'])]

            say("Free F's: {}".format(freeFactories))

            # take the service provided by the most F's
            try:
                f = random.choice(self.myAgent.possibleTakeovers[random.choice(self.myAgent.possibleTakeovers.keys())])
                # f = random.choice(self.myAgent.possibleTakeovers[
                #     max(self.myAgent.possibleTakeovers,
                #         key=lambda x: len(self.myAgent.possibleTakeovers[x]))])
                # if the F is free, and F's Volume ratio is under the set threshold
                say("{}: I chose to examine {}.".format(self.myAgent.getName(), f))
                # if (f in freeFactories and
                #         len([ed for ed in N.getEdges() if '~' + f in ed]) / self.myAgent.productionVolume <= self.myAgent.volumeThreshold):

                if (f in freeFactories and
                    G.node[int(f.split("@")[0])]['productionVolume'] /
                        self.myAgent.productionVolume <=
                        self.myAgent.volumeThreshold):

                    receiver = spade.AID.aid(
                        name=f,
                        addresses=["xmpp://{}".format(f)])
                    msg = spade.ACLMessage.ACLMessage()
                    msg.setPerformative("propose-takeover")
                    msg.setOntology("takeovers")
                    msg.addReceiver(receiver)
                    msg.setContent(self.myAgent.productionVolume)
                    self.myAgent.send(msg)
            except Exception as e:
                say("Caught error: {}".format(e))

        def _process(self):
            pass

    def _setup(self):
        if visualise:
            self.node = N.addNode(
                self.getName(),
                shape='square',
                color=FactoryColours[self.getName()],
                radius=30,
                label='{} ({} BTC)'.format(self.name, self.moneyOwned).capitalize(),  # remove '@127.0.0.1' from node name re.sub('[!@#$]', '', line)
                title='{} {}'.format(self.name, self.offeredServices).capitalize()
                )
            N.log('<p>{} successfully created.</p>'.format(self.getName()))
            network['nodes']['factories'][self]['node'] = self.node

        self.occupied = False
        self.checkAcquisitions = False
        self.productionCounter = 0
        self.volumeThreshold = random.randint(60, 90)/100.0
        self.priceWeight = 1
        self.productionVolume = 0
        self.myFactories = []

        print(self.name)

        G.node[int(self.name)]['money'] = self.moneyOwned
        G.node[int(self.name)]['name'] = self.name
        G.node[int(self.name)]['type'] = self.factoryType
        G.node[int(self.name)]['priceWeight'] = self.priceWeight
        G.node[int(self.name)]['productionVolume'] = self.productionVolume
        G.node[int(self.name)]['ownership'] = self.name
        G.node[int(self.name)]['offeredServices'] = self.offeredServices
        G.node[int(self.name)]['volumeThreshold'] = self.volumeThreshold
        G.node[int(self.name)]['time'] = 0

        # register with Agent Charter -- add the F's data series
        msg = spade.ACLMessage.ACLMessage()
        receiver = spade.AID.aid(
            name='chart5@127.0.0.1',
            addresses=['xmpp://chart5@127.0.0.1'])
        msg.addReceiver(receiver)
        msg.setOntology('chart')
        msg.setPerformative('inform-start')
        msg.setContent(self.moneyOwned)
        self.send(msg)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setPerformative("propose")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.AnswerQuery(), t)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setPerformative("request")
        tmplt.setOntology("recipeParts")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.Produce(), t)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setOntology("takeovers")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.AnswerTakeoverNegotiation(), t)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setOntology("money")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.TakeMoney(), t)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setOntology("chart")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.ProvideData(), t)

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setOntology("termination")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.Terminate(), t)


class AgentCharter(spade.Agent.Agent):
    class CheckStats(spade.Behaviour.PeriodicBehaviour):
        def _process(self):
            self.myAgent.TimeCounter += 1
            print("Tick: {}".format(self.myAgent.TimeCounter))

            aad = spade.AMS.AmsAgentDescription()
            res = self.myAgent.searchAgent(aad)

            if len(res) + 3 < numOfFactories:
                print("Nothing to do here yet...")
                return

            if self.myAgent.TimeCounter % 10 == 0:
                msg = spade.ACLMessage.ACLMessage()
                try:
                    for k in FactoryIDs:
                        receiver = spade.AID.aid(
                            name="{}@127.0.0.1".format(k),
                            addresses=["xmpp://{}@127.0.0.1".format(k)])
                        msg.addReceiver(receiver)
                    msg.setOntology("chart")
                    self.myAgent.send(msg)
                except Exception as e:
                    print(e)
                # msg.setPerformative("request")

                with open(self.myAgent.dataFileName, 'a') as csvfile:
                    for d in G.nodes().data():
                        data = d[1]
                        data['time'] = self.myAgent.TimeCounter
                        fieldnames = data.keys()
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow(data)

                if not self.myAgent.oldGraph:
                    self.myAgent.oldGraph = [
                        (G.node[n]['name'],
                            G.node[n]['money'],
                            G.node[n]['productionVolume'])
                        for n in G.nodes()]
                    # self.myAgent.oldGraph = list(G.nodes(data=True))
                    say(self.myAgent.oldGraph)

            if self.myAgent.TimeCounter % 20 == 0:
                self.myAgent.newGraph = [
                        (G.node[n]['name'],
                            G.node[n]['money'],
                            G.node[n]['productionVolume'])
                        for n in G.nodes()]
                # self.myAgent.newGraph = list(G.nodes(data=True))
                say("{}\nvs.\n{}".format(self.myAgent.oldGraph, self.myAgent.newGraph))
                # if the Old and New graphs are different, proceed, otherwise kill all
                if self.myAgent.oldGraph != self.myAgent.newGraph:
                    say("Terminate NOT")
                    self.myAgent.oldGraph = self.myAgent.newGraph
                    say(G.nodes())
                    self.myAgent.terminationImminent = False
                else:
                    if self.myAgent.terminationImminent:
                        print("Terminate NOW")
                        msg = spade.ACLMessage.ACLMessage()
                        for k in FactoryIDs:
                            receiver = spade.AID.aid(
                                name="{}@127.0.0.1".format(k),
                                addresses=["xmpp://{}@127.0.0.1".format(k)])
                            msg.addReceiver(receiver)
                        # msg.setPerformative("request")
                        msg.setOntology("termination")
                        self.myAgent.send(msg)

                        time.sleep(5)

                        self.myAgent._kill()
                    else:
                        print("The end is nigh!")
                        self.myAgent.terminationImminent = True

            # time.sleep(1)

    class AcceptData(spade.Behaviour.EventBehaviour):
        def onStart(self):
            msg = self._receive()

            if charting:
                if msg.getPerformative() == 'inform-start':
                    C.addSeries(
                        re.sub(
                            '@127.0.0.1',
                            '',
                            msg.getSender().getName()).capitalize(),
                        [1],
                        [int(msg.getContent())])

                elif msg.getPerformative() == 'inform-value':
                    C.addValue(
                        re.sub(
                            '@127.0.0.1',
                            '',
                            msg.getSender().getName()).capitalize(),
                        self.myAgent.TimeCounter,
                        int(msg.getContent()))

    def _setup(self):
        print("Charter starting!")
        self.TimeCounter = 1

        tmplt = spade.Behaviour.ACLTemplate()
        tmplt.setOntology("chart")
        t = spade.Behaviour.MessageTemplate(tmplt)

        self.addBehaviour(self.AcceptData(), t)

        time.sleep(3*numOfFactories)
        # res = None
        # while not res:
        #     try:
        #         aad = spade.AMS.AmsAgentDescription()
        #         res = self.searchAgent(aad)
        #         time.sleep(1)
        #     except Exception as e:
        #         print e
        # print("{} ? {}".format(len(res), numOfFactories))
        # while len(res) < numOfFactories:
        #     try:
        #         aad = spade.AMS.AmsAgentDescription()
        #         res = self.searchAgent(aad)
        #         print("I'm waiting ({}).".format(len(res)))
        #     except Exception as e:
        #         raise e
        #     time.sleep(2)

        ID = '{:%Y%m%d%H%M%S}'.format(datetime.now())

        self.dataFileName = 'simData{}.csv'.format(ID)
        with open(self.dataFileName, 'a') as csvfile:
            fieldnames = G.node[list(G.nodes())[0]].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        dataFileName = 'simData.csv'
        data = {'ID': ID,
                'ServicePrices': priceOfService,
                'OrderMoneyStartMin': OrderMoneyStartMin,
                'OrderMoneyStartMax': OrderMoneyStartMax,
                'FactoryMoneyStart': FactoryMoneyStart,
                'NoOfFactories': numOfFactories,
                'NoOfOrders': numOfOrders,
                'NoOfServices': numOfServices,
                'NoOfRecipePieces': numOfRecipePieces,
                'NoOfServicesPerFactory': numOfServicesPerFactory
                }
        if not os.path.isfile(dataFileName):
            fileIsNew = True
        else:
            fileIsNew = False
        with open(dataFileName, 'a') as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if fileIsNew is True:
                writer.writeheader()
            writer.writerow(data)

        self.terminationImminent = False
        self.oldGraph = None

        self.addBehaviour(self.CheckStats(1), None)


if __name__ == "__main__":
    # random.seed(16)

    if numOfFactories:
        # generate graph G with numOfFactories nodes
        # with edge creation probability of 0.2
        G = nx.gnp_random_graph(numOfFactories, 0.3)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(50, 500)
        FactoryIDs = random.sample(range(50000, 60000), numOfFactories)
    else:
        # list of edges as (n1, n2, weight)
        raw = [
            ('zagreb',      'ljubljana',222),
            ('varazdin',    'zagreb',   80),
            ('zagreb',      'rijeka',   300),
            ('rijeka',      'pula',     150),
            ('pula',        'trst',     170),
            ('rijeka',      'trst',     100),
            ('rijeka',      'dubrovnik',700),
            ('rijeka',      'zadar',    300),
            ('zadar',       'dubrovnik',410),
            ('zadar',       'varazdin', 400),
            ('osijek',      'zagreb',   300)
        ]

        edges = []

        for r in raw:
            edges.append(
                    (
                        '{}'.format(r[0]).lower(),
                        '{}'.format(r[1]).lower(),
                        r[2]
                    )
                )

        G.add_weighted_edges_from(edges)
        numOfFactories = len(list(G.nodes()))

    print(G.nodes())
    print(G.edges().data())

    if not G.nodes():
        FactoryIDs = random.sample(range(50000, 60000), numOfFactories)
    else:
        FactoryIDs = list(G.nodes())
        numOfFactories = len(FactoryIDs)
    OrderIDs = random.sample(range(1000, 10000), int(numOfOrders * 1.5))

    availableColours = [random.uniform(0, 0xFFFFFF) for f in FactoryIDs]
    FactoryColours = {"{}@127.0.0.1".format(f): "#{:06x}".format(int(availableColours[f])) for f in FactoryIDs}

    # defining agents, named factoryX,
    # with appended services
    regFactoryServices = []
    AgentFactories = []

    # time.sleep(1)

    charter = AgentCharter("chart@127.0.0.1", "tajniChart")
    charter.start()

    for x in FactoryIDs:
        agent = AgentFactory("{}@127.0.0.1".format(x), "tajna")

        if visualise:
            network['nodes']['factories'][agent] = {}

        # generate numOfServicesPerFactory services in range 1 to numOfServices+1
        agent.offeredServices = random.sample(
            range(1, numOfServices + 1),
            random.randint(1, numOfServicesPerFactory))

        agent.moneyOwned = FactoryMoneyStart

        agent.factoryType = random.choice(['Diversifier', 'Monopolist'])
        agent.name = int(x)


        # register offered services of the factory agent
        fS = spade.DF.DfAgentDescription()
        for x in agent.offeredServices:
            service = spade.DF.ServiceDescription()
            service.setName("Service{}".format(x))
            service.setType("Production")
            fS.addService(service)
        fS.setAID(agent.getAID())

        regS = agent.registerService(fS)
        regFactoryServices.append(regS)

        agent.start()
        time.sleep(1)

    if visualise:
        for e in G.edges().data():
            N.addEdge(
                "{}@127.0.0.1".format(e[0]),
                "{}@127.0.0.1".format(e[1]),
                length=e[2]['weight'],
                label=str(e[2]['weight']))

        time.sleep(0.2)

    def addOrder(nodes):
        x = OrderIDs.pop()
        agent = AgentOrder("order%s@127.0.0.1" % str(x), "tajna")

        agent.moneyOwned = random.randint(OrderMoneyStartMin, OrderMoneyStartMax)
        agent.agentID = x

        network['nodes']['orders'][agent] = {}
        network['nodes']['orders'][agent]['id'] = x

        agent.start()

        if visualise:
            N.log('Order agent {} started!'.format(x))

    for n in xrange(0, numOfOrders):
        addOrder(1)
        time.sleep(0.5)

    if visualise:
        N.addAction('Add new Order agent', addOrder)

# dva tipa factoryja: asortativnost, uspjeh, Fabac
