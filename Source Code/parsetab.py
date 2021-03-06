
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftPOWERBEGIN COLON COMMA DATA DIVIDE DO DOT ELSE END EQUALS FLOAT FOR GE GT ID IF INTEGER LE LPAREN LT MINUS MOD NE NEWLINE PLUS POWER PROGRAM RPAREN SEMI STRING THEN TIMES TO VAR WRITE WRITELNprogram : program statement\n               | statementprogram : errorstatement : INTEGER command NEWLINEstatement : INTEGER error NEWLINEstatement : NEWLINEstatement : INTEGER NEWLINEcommand : DATA numlistcommand : DATA errorcommand : WRITELN LPAREN wlist RPAREN endingcommand : WRITELN errorcommand : WRITELN endingcommand : WRITE LPAREN wlist RPAREN endingcommand : WRITE errorcommand : WRITE LPAREN RPAREN endingcommand : PROGRAM variable endingcommand : VAR varlist COLON variable endingcommand : VAR errorcommand : variable COLON variable endingcommand : variable errorcommand : variable COLON EQUALS expr SEMIvarlist : varlist COMMA variable\n               | variableexpr : INTEGER\n            | FLOATexpr : variableexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr POWER expr\n            | expr MOD expr variable : IDcommand : END DOTcommand : BEGINending : SEMIcommand : IF LPAREN relexpr RPAREN THEN INTEGER INTEGERcommand : IF LPAREN error RPAREN THEN INTEGER INTEGERcommand : IF LPAREN relexpr RPAREN THEN errorcommand : ELSEcommand : END endingcommand : END ending INTEGER INTEGERcommand : END INTEGERrelexpr : expr LT expr\n               | expr LE expr\n               | expr GT expr\n               | expr GE expr\n               | expr EQUALS expr\n               | expr NE exprcommand : FOR variable COLON EQUALS expr TO expr DO INTEGER INTEGERwlist   : wlist COMMA witem\n               | witemwitem : STRINGwitem : exprnumlist : numlist COMMA number\n               | numbernumber  : INTEGER\n               | FLOAT'
    
_lr_action_items = {'error':([0,4,10,11,12,14,15,21,44,102,],[3,9,25,31,34,37,40,-33,63,112,]),'INTEGER':([0,1,2,3,5,6,8,10,16,22,23,29,32,33,42,44,46,58,61,68,69,70,71,72,73,74,84,85,86,87,88,89,90,102,103,111,113,114,118,119,],[4,4,-2,-3,-6,-1,-7,27,43,-4,-5,51,-36,51,61,51,27,51,81,51,51,51,51,51,51,51,51,51,51,51,51,51,51,111,113,115,116,51,119,120,]),'NEWLINE':([0,1,2,3,4,5,6,7,8,9,17,19,22,23,24,25,26,27,28,30,31,32,34,37,40,41,42,43,56,66,76,77,81,91,99,100,101,112,115,116,120,],[5,5,-2,-3,8,-6,-1,22,-7,23,-35,-40,-4,-5,-8,-9,-56,-57,-58,-12,-11,-36,-14,-20,-18,-34,-41,-43,-16,-55,-15,-19,-42,-10,-13,-21,-17,-39,-37,-38,-50,]),'$end':([1,2,3,5,6,8,22,23,],[0,-2,-3,-6,-1,-7,-4,-5,]),'DATA':([4,],[10,]),'WRITELN':([4,],[11,]),'WRITE':([4,],[12,]),'PROGRAM':([4,],[13,]),'VAR':([4,],[15,]),'END':([4,],[16,]),'BEGIN':([4,],[17,]),'IF':([4,],[18,]),'ELSE':([4,],[19,]),'FOR':([4,],[20,]),'ID':([4,13,15,20,29,33,36,44,58,59,60,68,69,70,71,72,73,74,84,85,86,87,88,89,90,114,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'FLOAT':([10,29,33,44,46,58,68,69,70,71,72,73,74,84,85,86,87,88,89,90,114,],[28,52,52,52,28,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'LPAREN':([11,12,18,],[29,33,44,]),'SEMI':([11,16,21,35,51,52,53,55,57,67,75,78,79,93,94,95,96,97,98,],[32,32,-33,32,-24,-25,-26,32,32,32,32,100,32,-27,-28,-29,-30,-31,-32,]),'COLON':([14,21,38,39,45,80,],[36,-33,59,-23,65,-22,]),'DOT':([16,],[41,]),'COMMA':([21,24,26,27,28,38,39,47,48,49,50,51,52,53,54,66,80,92,93,94,95,96,97,98,],[-33,46,-56,-57,-58,60,-23,68,-52,-53,-54,-24,-25,-26,68,-55,-22,-51,-27,-28,-29,-30,-31,-32,]),'PLUS':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,69,-24,-25,-26,69,69,-27,-28,-29,-30,-31,69,69,69,69,69,69,69,69,69,]),'MINUS':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,70,-24,-25,-26,70,70,-27,-28,-29,-30,-31,70,70,70,70,70,70,70,70,70,]),'TIMES':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,71,-24,-25,-26,71,71,71,71,-29,-30,-31,71,71,71,71,71,71,71,71,71,]),'DIVIDE':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,72,-24,-25,-26,72,72,72,72,-29,-30,-31,72,72,72,72,72,72,72,72,72,]),'POWER':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,73,-24,-25,-26,73,73,73,73,73,73,-31,73,73,73,73,73,73,73,73,73,]),'MOD':([21,50,51,52,53,64,78,93,94,95,96,97,98,104,105,106,107,108,109,110,117,],[-33,74,-24,-25,-26,74,74,-27,-28,-29,-30,-31,74,74,74,74,74,74,74,74,74,]),'RPAREN':([21,33,47,48,49,50,51,52,53,54,62,63,92,93,94,95,96,97,98,104,105,106,107,108,109,],[-33,55,67,-52,-53,-54,-24,-25,-26,75,82,83,-51,-27,-28,-29,-30,-31,-32,-44,-45,-46,-47,-48,-49,]),'LT':([21,51,52,53,64,93,94,95,96,97,98,],[-33,-24,-25,-26,84,-27,-28,-29,-30,-31,-32,]),'LE':([21,51,52,53,64,93,94,95,96,97,98,],[-33,-24,-25,-26,85,-27,-28,-29,-30,-31,-32,]),'GT':([21,51,52,53,64,93,94,95,96,97,98,],[-33,-24,-25,-26,86,-27,-28,-29,-30,-31,-32,]),'GE':([21,51,52,53,64,93,94,95,96,97,98,],[-33,-24,-25,-26,87,-27,-28,-29,-30,-31,-32,]),'EQUALS':([21,36,51,52,53,64,65,93,94,95,96,97,98,],[-33,58,-24,-25,-26,88,90,-27,-28,-29,-30,-31,-32,]),'NE':([21,51,52,53,64,93,94,95,96,97,98,],[-33,-24,-25,-26,89,-27,-28,-29,-30,-31,-32,]),'TO':([21,51,52,53,93,94,95,96,97,98,110,],[-33,-24,-25,-26,-27,-28,-29,-30,-31,-32,114,]),'DO':([21,51,52,53,93,94,95,96,97,98,117,],[-33,-24,-25,-26,-27,-28,-29,-30,-31,-32,118,]),'STRING':([29,33,68,],[49,49,49,]),'THEN':([82,83,],[102,103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,6,]),'command':([4,],[7,]),'variable':([4,13,15,20,29,33,36,44,58,59,60,68,69,70,71,72,73,74,84,85,86,87,88,89,90,114,],[14,35,39,45,53,53,57,53,53,79,80,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'numlist':([10,],[24,]),'number':([10,46,],[26,66,]),'ending':([11,16,35,55,57,67,75,79,],[30,42,56,76,77,91,99,101,]),'varlist':([15,],[38,]),'wlist':([29,33,],[47,54,]),'witem':([29,33,68,],[48,48,92,]),'expr':([29,33,44,58,68,69,70,71,72,73,74,84,85,86,87,88,89,90,114,],[50,50,64,78,50,93,94,95,96,97,98,104,105,106,107,108,109,110,117,]),'relexpr':([44,],[62,]),}

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
  ('statement -> INTEGER NEWLINE','statement',2,'p_statement_blank','PascalParse.py',67),
  ('command -> DATA numlist','command',2,'p_command_data','PascalParse.py',71),
  ('command -> DATA error','command',2,'p_command_data_bad','PascalParse.py',76),
  ('command -> WRITELN LPAREN wlist RPAREN ending','command',5,'p_command_writeln','PascalParse.py',82),
  ('command -> WRITELN error','command',2,'p_command_writeln_bad','PascalParse.py',87),
  ('command -> WRITELN ending','command',2,'p_command_writeln_empty','PascalParse.py',91),
  ('command -> WRITE LPAREN wlist RPAREN ending','command',5,'p_command_write','PascalParse.py',96),
  ('command -> WRITE error','command',2,'p_command_write_bad','PascalParse.py',101),
  ('command -> WRITE LPAREN RPAREN ending','command',4,'p_command_write_empty','PascalParse.py',105),
  ('command -> PROGRAM variable ending','command',3,'p_command_program','PascalParse.py',113),
  ('command -> VAR varlist COLON variable ending','command',5,'p_command_var','PascalParse.py',122),
  ('command -> VAR error','command',2,'p_command_var_error','PascalParse.py',127),
  ('command -> variable COLON variable ending','command',4,'p_command_declare','PascalParse.py',132),
  ('command -> variable error','command',2,'p_command_declare_error','PascalParse.py',137),
  ('command -> variable COLON EQUALS expr SEMI','command',5,'p_command_assign','PascalParse.py',142),
  ('varlist -> varlist COMMA variable','varlist',3,'p_command_varlist','PascalParse.py',147),
  ('varlist -> variable','varlist',1,'p_command_varlist','PascalParse.py',148),
  ('expr -> INTEGER','expr',1,'p_command_value','PascalParse.py',156),
  ('expr -> FLOAT','expr',1,'p_command_value','PascalParse.py',157),
  ('expr -> variable','expr',1,'p_command_variable','PascalParse.py',161),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binary','PascalParse.py',165),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binary','PascalParse.py',166),
  ('expr -> expr TIMES expr','expr',3,'p_expr_binary','PascalParse.py',167),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_binary','PascalParse.py',168),
  ('expr -> expr POWER expr','expr',3,'p_expr_binary','PascalParse.py',169),
  ('expr -> expr MOD expr','expr',3,'p_expr_binary','PascalParse.py',170),
  ('variable -> ID','variable',1,'p_variable','PascalParse.py',178),
  ('command -> END DOT','command',2,'p_command_end','PascalParse.py',182),
  ('command -> BEGIN','command',1,'p_command_begin','PascalParse.py',187),
  ('ending -> SEMI','ending',1,'p_ending','PascalParse.py',193),
  ('command -> IF LPAREN relexpr RPAREN THEN INTEGER INTEGER','command',7,'p_command_if','PascalParse.py',201),
  ('command -> IF LPAREN error RPAREN THEN INTEGER INTEGER','command',7,'p_command_if_bad','PascalParse.py',206),
  ('command -> IF LPAREN relexpr RPAREN THEN error','command',6,'p_command_if_bad2','PascalParse.py',210),
  ('command -> ELSE','command',1,'p_command_else','PascalParse.py',214),
  ('command -> END ending','command',2,'p_command_endelseif','PascalParse.py',219),
  ('command -> END ending INTEGER INTEGER','command',4,'p_command_endfor','PascalParse.py',223),
  ('command -> END INTEGER','command',2,'p_command_endif','PascalParse.py',227),
  ('relexpr -> expr LT expr','relexpr',3,'p_relexpr','PascalParse.py',232),
  ('relexpr -> expr LE expr','relexpr',3,'p_relexpr','PascalParse.py',233),
  ('relexpr -> expr GT expr','relexpr',3,'p_relexpr','PascalParse.py',234),
  ('relexpr -> expr GE expr','relexpr',3,'p_relexpr','PascalParse.py',235),
  ('relexpr -> expr EQUALS expr','relexpr',3,'p_relexpr','PascalParse.py',236),
  ('relexpr -> expr NE expr','relexpr',3,'p_relexpr','PascalParse.py',237),
  ('command -> FOR variable COLON EQUALS expr TO expr DO INTEGER INTEGER','command',10,'p_command_for','PascalParse.py',245),
  ('wlist -> wlist COMMA witem','wlist',3,'p_wlist','PascalParse.py',252),
  ('wlist -> witem','wlist',1,'p_wlist','PascalParse.py',253),
  ('witem -> STRING','witem',1,'p_item_string','PascalParse.py',264),
  ('witem -> expr','witem',1,'p_item_expr','PascalParse.py',270),
  ('numlist -> numlist COMMA number','numlist',3,'p_numlist','PascalParse.py',279),
  ('numlist -> number','numlist',1,'p_numlist','PascalParse.py',280),
  ('number -> INTEGER','number',1,'p_number','PascalParse.py',292),
  ('number -> FLOAT','number',1,'p_number','PascalParse.py',293),
]
