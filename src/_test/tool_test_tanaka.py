# -*- coding: utf-8 -*-
#ツールテスト
import maya.cmds as cmds
class tool_test(object):
	def __init__(self):
		self.win = u"tool_test_tanaka"
		if ( cmds.window(self.win,exists=True)):cmds.deleteUI(self.win)
		win = cmds.window(self.win,tlb=True)
		cmds.showWindow(win)
tool_test()