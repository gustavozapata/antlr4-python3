grammar fspow ;
//program
prog:   stat+ ;
//statement
stat:   fcCreation ;
fcCreation: 
        ID '=' fcCreationName '(' rootSpecifier ')' ;
fcCreationName: 'FileCollection' ;
rootSpecifier:  STRING ;

ID:     [a-zA-Z][a-zA-Z0-9]+ ;
STRING: '"'.*?'"' ; //match anything in " " (double quotes)
WS:     [ \t\r\n]+ -> skip ;
