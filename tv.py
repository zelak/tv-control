#
# Remove TV Control class
#

import lg

class TV:

    # List of TV manufacturers and models.
    tvs = {
        'LG' : lg.LG()
    }

    # Class constructor
    # @arg model TV model
    def __init__(self, model):
        self.cmds = self.tvs[model].cmds
        self.serial = self.tvs[model].serial

    # Command a TV
    # @arg cmd   TV command
    # @arg value Optional command value
    def cmd(self, cmd, value=0):
        print self.cmds[cmd]
