"""$Id: text_plain.py 699 2006-09-25 02:01:18Z rubys $"""

__author__ = "Sam Ruby <http://intertwingly.net/> and Mark Pilgrim <http://diveintomark.org/>"
__version__ = "$Revision: 699 $"
__date__ = "$Date: 2006-09-25 02:01:18 +0000 (Mon, 25 Sep 2006) $"
__copyright__ = "Copyright (c) 2002 Sam Ruby and Mark Pilgrim"

"""Output class for plain text output"""

from base import BaseFormatter
import feedvalidator

class Formatter(BaseFormatter):
  def format(self, event):
    return '%s %s%s' % (self.getLineAndColumn(event), self.getMessage(event),
      self.getCount(event))
