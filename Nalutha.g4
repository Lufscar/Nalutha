grammar Nalutha;

/*
    Declaração das regras léxicas
*/
Id: ('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
Num: [0-9]+;

fragment
ESC_SEQ	: '\\\'';
WS: ( ' ' | '\t' | '\r' | '\n') -> skip;

// Regra para verificação de erro léxico
ERRO: .;

/*
    Declaração das regras sintáticas
*/
program: config model EOF;
config: 'Project' ':' projectName=Id 'Api name' ':' apiName=Id;
model: 'Model' '{' entity* '}';
entity: 'Entity' Id '{' field+ '}';
field: fieldName=Id ':' fieldType=Id ('[' fieldSize=Num ']')?;