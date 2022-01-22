
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN COMMA DATA DOT END FLOAT ID INTEGER LPAREN NEWLINE PROGRAM RPAREN SEMI STRING VAR WRITELNprogram : program statement\n               | statementprogram : errorstatement : INTEGER command NEWLINEstatement : INTEGER error NEWLINEstatement : NEWLINEstatement : INTEGER NEWLINEcommand : DATA numlistcommand : DATA errorcommand : WRITELN LPAREN wlist RPAREN endingcommand : WRITELN errorcommand : WRITELN LPAREN RPAREN endingcommand : PROGRAM variable endingvariable : IDcommand : END DOTcommand : BEGINending : SEMIwlist   : wlist COMMA ID\n               | witemwitem : STRINGnumlist : numlist COMMA number\n               | numbernumber  : INTEGER\n               | FLOAT'
    
_lr_action_items = {'error':([0,4,10,11,],[3,9,18,23,]),'INTEGER':([0,1,2,3,5,6,8,10,15,16,27,],[4,4,-2,-3,-6,-1,-7,20,-4,-5,20,]),'NEWLINE':([0,1,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,21,23,26,32,33,34,37,38,],[5,5,-2,-3,8,-6,-1,15,-7,16,-16,-4,-5,-8,-9,-22,-23,-24,-11,-15,-13,-17,-21,-12,-10,]),'$end':([1,2,3,5,6,8,15,16,],[0,-2,-3,-6,-1,-7,-4,-5,]),'DATA':([4,],[10,]),'WRITELN':([4,],[11,]),'PROGRAM':([4,],[12,]),'END':([4,],[13,]),'BEGIN':([4,],[14,]),'FLOAT':([10,27,],[21,21,]),'LPAREN':([11,],[22,]),'ID':([12,36,],[25,39,]),'DOT':([13,],[26,]),'COMMA':([17,19,20,21,28,30,31,34,39,],[27,-22,-23,-24,36,-19,-20,-21,-18,]),'RPAREN':([22,28,30,31,39,],[29,35,-19,-20,-18,]),'STRING':([22,],[31,]),'SEMI':([24,25,29,35,],[33,-14,33,33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,6,]),'command':([4,],[7,]),'numlist':([10,],[17,]),'number':([10,27,],[19,34,]),'variable':([12,],[24,]),'wlist':([22,],[28,]),'witem':([22,],[30,]),'ending':([24,29,35,],[32,37,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','PascalParse.py',16),
  ('program -> statement','program',1,'p_program','PascalParse.py',17),
  ('program -> error','program',1,'p_program_error','PascalParse.py',33),
  ('statement -> INTEGER command NEWLINE','statement',3,'p_statement','PascalParse.py',40),
  ('statement -> INTEGER error NEWLINE','statement',3,'p_statement_bad','PascalParse.py',55),
  ('statement -> NEWLINE','statement',1,'p_statement_newline','PascalParse.py',62),
  ('statement -> INTEGER NEWLINE','statement',2,'p_statement_blank','PascalParse.py',73),
  ('command -> DATA numlist','command',2,'p_command_data','PascalParse.py',77),
  ('command -> DATA error','command',2,'p_command_data_bad','PascalParse.py',82),
  ('command -> WRITELN LPAREN wlist RPAREN ending','command',5,'p_command_writeln','PascalParse.py',87),
  ('command -> WRITELN error','command',2,'p_command_writeln_bad','PascalParse.py',92),
  ('command -> WRITELN LPAREN RPAREN ending','command',4,'p_command_writeln_empty','PascalParse.py',96),
  ('command -> PROGRAM variable ending','command',3,'p_command_program','PascalParse.py',101),
  ('variable -> ID','variable',1,'p_variable','PascalParse.py',108),
  ('command -> END DOT','command',2,'p_command_end','PascalParse.py',112),
  ('command -> BEGIN','command',1,'p_command_begin','PascalParse.py',117),
  ('ending -> SEMI','ending',1,'p_ending','PascalParse.py',123),
  ('wlist -> wlist COMMA ID','wlist',3,'p_wlist','PascalParse.py',138),
  ('wlist -> witem','wlist',1,'p_wlist','PascalParse.py',139),
  ('witem -> STRING','witem',1,'p_item_string','PascalParse.py',148),
  ('numlist -> numlist COMMA number','numlist',3,'p_numlist','PascalParse.py',159),
  ('numlist -> number','numlist',1,'p_numlist','PascalParse.py',160),
  ('number -> INTEGER','number',1,'p_number','PascalParse.py',172),
  ('number -> FLOAT','number',1,'p_number','PascalParse.py',173),
]
