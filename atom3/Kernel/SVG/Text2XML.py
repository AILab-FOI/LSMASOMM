"""
Text2XML.py

By Denis Dube, 2006
"""

def Text2XML(textString):
  """
  Parameter:
    textString = A regular string
  Return:
    String with all XML reserved characters replaced by their escape characters
    
  Info (http://hdf.ncsa.uiuc.edu/HDF5/XML/xml_escape_chars.htm):
    quote (")   &quot;
    apostrophe (')   &apos;
    ampersand (&)   &amp;
    less than (<)   &lt;
    greater than (>)   &gt;
  """
  XML = textString.replace('&', '&amp;').replace('<', '&lt;')
  XML = XML.replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')
  return XML
  
  

