grammar Nalutha;

/*
    Declaração das regras léxicas
*/
Id: ('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
model_lex: 'Model';
entity_lex: 'Entity';
dois_pontos: ':';
abre_chave: '{';
fecha_chave: '}';

fragment
ESC_SEQ	: '\\\'';
WS: ( ' ' | '\t' | '\r' | '\n') -> skip;

// Regra para verificação de erro léxico
ERRO: .;

/*
    Declaração das regras sintáticas
*/
program: model EOF;
model: 'Model' '{' entity* '}';
entity: 'Entity' Id '{' field+ '}';
field: fieldName=Id ':' fieldType=Id;