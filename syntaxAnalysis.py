import re

import ply.yacc as yacc

from lexicalAnalysis import tokens


## APORTACIÓN JEREMY POVEDA
# Regla para permitir más de una instrucción
def p_inicial_program(p):
    """inicial_program : PHP_IDENTIFIER program PHP_END_IDENTIFIER"""

def p_program_sentence_program(p):
    """program : sentence program """


def p_program_sentence(p):
    """program : sentence"""


# Sentencias para impresión de valores, asignaciones, estructuras de datos, declaración de funciones y estructuras de control.
def p_sentence_print_statement(p):
    """
    sentence : print_statement SEMICOLON
             | assignment SEMICOLON
             | types_structure
             | class_declaration
             | interface_declaration
             | control_structures
             | function_declaration
    """


# Estructuras de control
def p_control_structures(p):
    """
    control_structures : if_statement
                       | while_statement
                       | for_statement
    """


def p_while_statement(p):
    """
    while_statement : WHILE LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
    """


def p_if_statement(p):
    """
    if_statement : IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
                 | IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE elseif_statement
                 | IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE else_statement
    """


def p_elseif_statement(p):
    """
    elseif_statement : ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
                 | ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE elseif_statement
                 | ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE else_statement
    """


def p_else_statement(p):
    """
    else_statement : ELSE LEFT_BRACE body_statement RIGHT_BRACE
    """


def p_body_statement(p):
    """
    body_statement : sentence
            | sentence RETURN values SEMICOLON
            | sentence RETURN SEMICOLON
            | sentence BREAK SEMICOLON
            | sentence body_statement
            | RETURN values SEMICOLON
            | BREAK SEMICOLON
            | RETURN printable_values SEMICOLON
            | sentence RETURN printable_values SEMICOLON
    """
# Fin de aportacion Jeremy Poveda

#Aportacion Jorge Mawyin
def p_for_statement(p):
    """
    for_statement : FOR LEFT_PAREN VARIABLE EQUALS expression_for SEMICOLON condition_for SEMICOLON increment_statement RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
    """

def p_increment_statement(p):
    """
    increment_statement : VARIABLE INCREASE
                        | VARIABLE DECREMENT
                        | INCREASE VARIABLE
                        | DECREMENT VARIABLE
                        | VARIABLE PLUS_EQUALS INTEGER
                        | VARIABLE EQUALS VARIABLE operator_aritmetic number_values
    """

def p_condition_for(p):
    """
    condition_for : VARIABLE comparator_operator expression_for
    """

def p_expression_for(p):
    """
    expression_for : VARIABLE
                   | number_values
                   | expression_for operator_aritmetic expression_for
                   | LEFT_PAREN expression_for RIGHT_PAREN
                   | IDENTIFIER LEFT_PAREN VARIABLE RIGHT_PAREN
                   | IDENTIFIER LEFT_PAREN access_array_element RIGHT_PAREN
                   | length_operations
    """

def p_number_values(p):
    """
    number_values : INTEGER
                  | FLOAT
    """

def p_operator_aritmetic(p):
    """
    operator_aritmetic : PLUS
                       | MINUS
                       | MULTIPLY
                       | DIVIDE
                       | MODULE
                       | POW
    """

# Sentencias que pueden ser condicionales, preprosiciones lógicas y combinaciones de estas comparaciones y que estas solo se puedan operar logicamente
# Regla Semantica Jeremy Poveda (Regla 1 de los booleanos en el informe del proyecto)
def p_conditional(p):
    """
    conditional  : boolean_expression
                 | boolean_expression logic_operator boolean_expression

    """

def p_conditional_error(p):
    """
    conditional  :  boolean_expression logic_operator error
                 |  error logic_operator boolean_expression

    """
    print("Error semántico: las expresiones booleanas solo pueden ser operadas por otras expresiones booleanas")


def p_logic_operator(p):
    """
    logic_operator  : LOGIC_AND
                    | LOGIC_OR
                    | LOGIC_XOR 
    """


def p_boolean_expression(p):
    """
    boolean_expression  : comparation
                        | VARIABLE
                        | IDENTIFIER
                        | LEFT_PAREN conditional RIGHT_PAREN
                        | logic_not_sentence
                        | logic_expression
    """

#Regla Semantica Kevin Roldan (Regla 2 de los booleanos en el informe del proyecto)
def p_logic_expression(p):
    """
    logic_expression : true_boolean_types logic_operator false_boolean_types
                     | false_boolean_types logic_operator true_boolean_types
    """

def p_true_boolean_types(p):
    """
    true_boolean_types : TRUE
                       | STRING
                       | INTEGER
                       | FLOAT
                       | VARIABLE
                       | IDENTIFIER
                       | ARRAY LEFT_PAREN values RIGHT_PAREN
    """

def p_false_boolean_types(p):
    """
    false_boolean_types : FALSE
                        | STRING
                        | INTEGER
                        | VARIABLE
                        | IDENTIFIER
                        | FLOAT
                        | ARRAY LEFT_PAREN RIGHT_PAREN
                        | NULL
    """
#Fin de Regla Semantica Kevin Roldan


#Aportacion Jorge Mawyin
def p_logic_not_sentence (p):
    """
    logic_not_sentence : LOGIC_NOT conditional
             | LOGIC_NOT VARIABLE
    """
#fin aportacion


def p_comparation(p):
    """
    comparation : values comparator_operator values
                | values comparator_operator expression
                | expression comparator_operator expression
                | VARIABLE EQUALS_EQUALS values
                | access_array_element EQUALS_EQUALS values
                | access_array_element EQUALS_EQUALS VARIABLE
                | VARIABLE EQUALS_EQUALS access_array_element
                | VARIABLE EQUALS_EQUALS VARIABLE
                | access_array_element EQUALS_EQUALS access_array_element
                | access_element_matrix EQUALS_EQUALS VARIABLE
                | VARIABLE EQUALS_EQUALS access_element_matrix
    """


def p_comparator_operator(p):
    """
    comparator_operator : EQUALS_EQUALS
                         | IDENTICAL
                         | NOT_EQUALS
                         | NOT_IDENTICAL
                         | SMALL_THAN
                         | GREATER_THAN
                         | SMALL_EQUALS_TO
                         | GREATER_EQUALS_TO
                         | SPACECRAFT
                         | NULL_FUSION
    """

#Regla Semantica Jeremy Poveda (Regla 1 de las cadenas en el informe del proyecto)
# Se permiten concatenaciones entre strings y otros valores.


def p_print_statement(p):
    """
    print_statement : ECHO LEFT_PAREN printable_values RIGHT_PAREN
                    | PRINT LEFT_PAREN printable_values RIGHT_PAREN
                    | ECHO printable_values
                    | PRINT printable_values
    """

def p_printable_values(p):
   """
    printable_values : values
                     | values printable_dividers printable_values
                     | VARIABLE
                     | VARIABLE printable_dividers printable_values
                     | VARIABLE STRING_CONCATENATION STRING
                     | conditional
                     | conditional printable_dividers printable_values
                     | structure_object_principal
                     | structure_object_principal printable_dividers printable_values
    """
def p_printable_values_error(p):
    """
    printable_values : values printable_dividers error
                     | VARIABLE printable_dividers error
                     | conditional printable_dividers error
                     | structure_object_principal printable_dividers error
    """
    print("Error semántico: La concatenación no es válida para ese valor")

def p_printable_dividers(p):
    """
    printable_dividers : COMMA
                       | STRING_CONCATENATION
    """

# Tipos de dato
def p_values(p):
    """
    values : INTEGER
           | STRING
           | FLOAT
           | boolean
    """


def p_boolean(p):
    """
    boolean : TRUE
            | FALSE
    """


def p_expression(p):
    """
    expression : term
               | term PLUS expression
               | term MINUS expression
    """


def p_term(p):
    """
    term : factor
         | factor MULTIPLY term
         | factor DIVIDE term
         | factor MODULE term
         | factor POW term
    """

#Regla Semantica Jorge Mawyin (Regla 1 de los Enteros en el informe del proyecto)

def p_factor(p):
    """
    factor : INTEGER
           | FLOAT
           | VARIABLE
           | LEFT_PAREN expression RIGHT_PAREN
           | STRING
    """
    if len(p) == 2:
        p[0] = p[1]
        if p.slice[1].type == 'STRING':
            try:
               p[0] = int(p[1][1:-1])  
            except ValueError:
                try:
                    p[0] = float(p[1][1:-1])  
                except ValueError:
                    print(f'Error de sintaxis en {p[1]} , valor no permitido para expresiones aritmeticas')
                    raise SyntaxError(f'Error de sintaxis en {p[1]} , valor no permitido para expresiones aritmeticas')
        
    elif p[1] == '(':
        p[0] = p[2]

#Fin de la Regla Semantica Jorge Mawyin


# FIN DE APORTACIÓN JEREMY POVEDA

# APORTACIÓN KEVIN ROLDAN


def p_assignment(p):
    """
    assignment : variable_assignment
               | constant_assignment
    """


def p_variable_assignment(p):
    """
    variable_assignment : VARIABLE assignment_operator values
                        | VARIABLE assignment_operator IDENTIFIER
                        | VARIABLE assignment_operator expression 
                        | VARIABLE assignment_operator function_invocation
                        | VARIABLE assignment_operator string_special_function
                        | VARIABLE assignment_operator array_special_function_structure
                        | VARIABLE assignment_operator types_structure 
                        | VARIABLE assignment_operator input 
                        | VARIABLE assignment_operator special_function
                        | VARIABLE assignment_operator conditional
                        | VARIABLE INCREASE 
                        | VARIABLE DECREMENT 
                        | INCREASE VARIABLE 
                        | DECREMENT VARIABLE 
    """


# Aportación Jeremy Poveda, Para que se apliquen más operadores de asignación
def p_assignment_operator(p):
    """
    assignment_operator : EQUALS
                        | PLUS_EQUALS
    """
##

def p_constant_assignment(p):
    """
    constant_assignment : const_syntax
                        | define_syntax
    """


def p_const_syntax(p):
    """
     const_syntax : CONST IDENTIFIER EQUALS values 
    """


def p_define_syntax(p):
    """
        define_syntax : DEFINE LEFT_PAREN STRING COMMA values RIGHT_PAREN 
    """
    constant_name = p[3][1:-1]

    if re.match(r'[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*', constant_name) is None:
        print(f"Error de sintaxis: nombre de constante '{constant_name}' no permitido")
        raise SyntaxError(f"Error de sintaxis: nombre de constante '{constant_name}' no permitido")


def p_function_invocation(p):
    """
    function_invocation : IDENTIFIER LEFT_PAREN params RIGHT_PAREN
                        | VARIABLE LEFT_PAREN params RIGHT_PAREN
    """


def p_params(p):
    """
    params : real_params
           | empty
    """


def p_real_params(p):
    """
    real_params : VARIABLE
                | values
                | real_params COMMA VARIABLE
                | real_params COMMA values
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) > 2:
        p[0] = p[1] + [p[3]]


def p_empty(p):
    """
    empty :
    """
    pass


# Creado por Jeremy Poveda, separando la declaración de la función con su asignación a una variable
def p_function_declaration(p):
    """
    function_declaration : FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN codeblock
    """
##

def p_special_function(p):
    """
    special_function : arrow_function
                     | anonymous_functions
    """


def p_arrow_function(p):
    """
    arrow_function : FN LEFT_PAREN params RIGHT_PAREN EQUALS GREATER_THAN codeblock
                   | FN LEFT_PAREN params RIGHT_PAREN EQUALS GREATER_THAN print_statement
                   | FN LEFT_PAREN params RIGHT_PAREN EQUALS GREATER_THAN expression
    """


def p_anonymous_functions(p):
    """
    anonymous_functions : FUNCTION LEFT_PAREN params RIGHT_PAREN codeblock
    """


def p_codeblock(p):
    """
    codeblock : LEFT_BRACE body_statement RIGHT_BRACE
    """


def p_input(p):
    """
    input : FEGTS LEFT_PAREN STDIN RIGHT_PAREN
          | READLINE LEFT_PAREN STRING RIGHT_PAREN
    """

#Regla Semantica Kevin Roldan (Regla 1 de los Operaciones de Longitud en el informe del proyecto)


def p_string_special_function(p):
    """
    string_special_function : STRLEN LEFT_PAREN string_param RIGHT_PAREN
                            | SUBSTR LEFT_PAREN string_param COMMA int_param RIGHT_PAREN
                            | SUBSTR LEFT_PAREN string_param COMMA int_param COMMA int_param RIGHT_PAREN
    """

def p_string_param(p):
    """
    string_param : STRING
                 | VARIABLE
                 | INTEGER
    """
    if len(p) == 2:
        p[0] = p[1]
        if p.slice[1].type == 'INTEGER':

            print(f'Error de sintaxis en {p[1]} , El parámetro de cadena de la funcion no puede ser un entero')
            raise SyntaxError(f'Error de sintaxis en {p[1]} , El parámetro de cadena de la funcion no puede ser un entero')
        
def p_int_param(p):
    """
    int_param : INTEGER
              | VARIABLE
              | STRING
    """
    if len(p) == 2:
        p[0] = p[1]
        if p.slice[1].type == 'STRING':

            print(f'Error de sintaxis en {p[1]} , El parámetro de entero de la funcion no puede ser un string')
            raise SyntaxError(f'Error de sintaxis en {p[1]} , El parámetro de entero de la funcion no puede ser un string')
        
#Fin de la Regla Semantica Kevin Roldan

#Regla Semantica Jorge Mawyin (Regla 2 de los Operaciones de Longitud en el informe del proyecto)
def p_array_special_function_structure(p):
    """
    array_special_function_structure : array_special_function
                                     | statement_array_special_function_error
    """

def p_array_special_function(p):
    """
    array_special_function : COUNT LEFT_PAREN structure_array_principal count_param RIGHT_PAREN
                           | COUNT LEFT_PAREN structure_matrix_principal count_param RIGHT_PAREN
                           | COUNT LEFT_PAREN VARIABLE count_param RIGHT_PAREN
                           | ARRAY_POP LEFT_PAREN VARIABLE RIGHT_PAREN
                           | ARRAY_SUM LEFT_PAREN VARIABLE RIGHT_PAREN
    """

def p_statement_array_special_function_error(p):
    """
    statement_array_special_function_error : COUNT LEFT_PAREN error count_param RIGHT_PAREN
                                           | ARRAY_POP LEFT_PAREN error RIGHT_PAREN
                                           | ARRAY_SUM LEFT_PAREN error RIGHT_PAREN
    """
    print ("Error semántico, parámetro incorrecto para las funciones de arreglos")

def p_count_param(p):
    """
    count_param : COMMA COUNT_NORMAL
                | COMMA COUNT_RECURSIVE
                |
    """
def p_length_operations(p):
    """
    length_operations : COUNT LEFT_PAREN structure_array_principal count_param RIGHT_PAREN
                      | COUNT LEFT_PAREN structure_matrix_principal count_param RIGHT_PAREN
                      | COUNT LEFT_PAREN VARIABLE count_param RIGHT_PAREN
                      | STRLEN LEFT_PAREN string_param RIGHT_PAREN
    """
#Fin de la Regla Semantica Jorge Mawyin

# FIN DE APORTACIÓN KEVIN ROLDAN

# INICIO DE APORTACIÓN JORGE MAWYIN
# ESTRUCTURAS DE DATOS


def p_types_structure(p):
    """
    types_structure : structure_array_principal
                    | structure_matrix_principal
                    | structure_object_principal
    """


# ARRAY
def p_structure_array_principal(p):
    """
    structure_array_principal : indexed_array
                              | associative_array
                              | access_array_stucture
                              | access_array_element         
    """


def p_indexed_array(p):
    """indexed_array : ARRAY LEFT_PAREN values_array_indexed RIGHT_PAREN"""


def p_associative_array(p):
    """associative_array : ARRAY LEFT_PAREN structure_array RIGHT_PAREN 
                         | ARRAY LEFT_BRACKET structure_array RIGHT_BRACKET
    """


def p_structure_array(p):
    """
    structure_array : key EQUALS GREATER_THAN values
                    | key EQUALS GREATER_THAN values COMMA structure_array
    """


def p_key(p):
    """
    key : INTEGER
        | STRING
    """


def p_values_array_indexed(p):
    """values_array_indexed : values
                            | values COMMA values_array_indexed
                            | object_creation
                            | object_creation COMMA values_array_indexed
                            | indexed_array
                            | indexed_array COMMA values_array_indexed
    """

def p_access_array_stucture(p):
    """
    access_array_stucture : access_array_element
                          | statement_access_array_element_error
    """

def p_access_array_element(p):
    """
    access_array_element : VARIABLE LEFT_BRACKET INTEGER RIGHT_BRACKET
                         | VARIABLE LEFT_BRACKET VARIABLE RIGHT_BRACKET
    """

def p_statement_access_array_element_error(p):
    """
    statement_access_array_element_error : VARIABLE LEFT_BRACKET error RIGHT_BRACKET
    """   
    print("Error semántico, parámetro incorrecto para indexar un arreglo")

# MATRIX
def p_structure_matrix_principal(p):
    """
    structure_matrix_principal : matrix_firstform
                               | matrix_secondform
                               | access_element_matrix SEMICOLON
                               | modify_element_matrix SEMICOLON
                               | add_element_matrix
    """


def p_matrix_firstform(p):
    """matrix_firstform : ARRAY LEFT_PAREN structure_matrix_first RIGHT_PAREN SEMICOLON"""


def p_matrix_secondform(p):
    """matrix_secondform : LEFT_BRACKET structure_matrix_second RIGHT_BRACKET SEMICOLON"""


def p_structure_matrix_second(p):
    """
    structure_matrix_second : LEFT_BRACKET values RIGHT_BRACKET
                            | LEFT_BRACKET values RIGHT_BRACKET COMMA structure_matrix_second
    """


def p_structure_matrix_first(p):
    """
    structure_matrix_first : ARRAY LEFT_PAREN values RIGHT_PAREN
                           | ARRAY LEFT_PAREN values RIGHT_PAREN COMMA structure_matrix_first
    """


def p_access_element_matrix(p):
    """
    access_element_matrix : VARIABLE LEFT_BRACKET INTEGER RIGHT_BRACKET LEFT_BRACKET INTEGER RIGHT_BRACKET
                          | VARIABLE LEFT_BRACKET VARIABLE RIGHT_BRACKET LEFT_BRACKET VARIABLE RIGHT_BRACKET
                          | VARIABLE LEFT_BRACKET VARIABLE RIGHT_BRACKET LEFT_BRACKET INTEGER RIGHT_BRACKET
                          | VARIABLE LEFT_BRACKET INTEGER RIGHT_BRACKET LEFT_BRACKET VARIABLE RIGHT_BRACKET
    """


def p_modify_element_matrix(p):
    """modify_element_matrix : access_element_matrix EQUALS values
                             | access_element_matrix EQUALS VARIABLE
                             
    """


def p_add_element_matrix(p):
    """add_element_matrix : VARIABLE LEFT_BRACKET RIGHT_BRACKET EQUALS indexed_array"""


# FIN DE APORTACIÓN JORGE MAWYIN

# INICIO DE APORTACIÓN KEVIN ROLDAN
# OBJECT
def p_structure_object_principal(p):
    """
    structure_object_principal : object_creation
                               | access_method_object
    """


def p_object_creation(p):
    """object_creation : NEW IDENTIFIER
                       | NEW IDENTIFIER LEFT_PAREN params RIGHT_PAREN """


def p_access_method_object(p):
    """access_method_object : VARIABLE MINUS GREATER_THAN function_invocation
                            | VARIABLE MINUS GREATER_THAN accessType
                            | VARIABLE MINUS GREATER_THAN accessType EQUALS values
                            | VARIABLE MINUS GREATER_THAN accessType EQUALS VARIABLE
                            | VARIABLE MINUS GREATER_THAN accessType EQUALS access_array_element
                            | access_array_element MINUS GREATER_THAN function_invocation
                            | access_array_element MINUS GREATER_THAN accessType
                            | access_array_element MINUS GREATER_THAN accessType EQUALS values
                            | access_array_element MINUS GREATER_THAN accessType EQUALS VARIABLE
                            | access_array_element MINUS GREATER_THAN accessType EQUALS access_array_element
                            """


def p_accessType(p):
    """
    accessType : IDENTIFIER LEFT_BRACKET INTEGER RIGHT_BRACKET
               | IDENTIFIER
    """


def p_class_declaration(p):
    """class_declaration : CLASS IDENTIFIER class_extends_opt class_implements_opt LEFT_BRACE class_body RIGHT_BRACE"""


def p_interface_declaration(p):
    """interface_declaration : INTERFACE IDENTIFIER class_extends_opt LEFT_BRACE interface_body RIGHT_BRACE"""


def p_interface_body(p):
    """interface_body : interface_body interface_method
                     |"""


def p_interface_method(p):
    """interface_method : visibility_opt FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN SEMICOLON"""


def p_class_extends_opt(p):
    """class_extends_opt : EXTENDS IDENTIFIER
                        | """


def p_class_implements_opt(p):
    """class_implements_opt : IMPLEMENTS interface_list
                           |"""


def p_interface_list(p):
    """interface_list : IDENTIFIER
                     | interface_list COMMA IDENTIFIER"""


def p_class_body(p):
    """class_body : class_body class_member
                  |"""


def p_class_member(p):
    """class_member : visibility_opt STATIC FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN LEFT_BRACE method_body RIGHT_BRACE
                    | visibility_opt FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN LEFT_BRACE method_body RIGHT_BRACE
                    | class_attribute """


def p_class_attribute(p):
    """
    class_attribute : visibility_opt VARIABLE  EQUALS values SEMICOLON
                    | visibility_opt VARIABLE SEMICOLON
                    | visibility_opt constant_assignment SEMICOLON
    """


def p_visibility_opt(p):
    """visibility_opt : PUBLIC
                     | PRIVATE
                     | PROTECTED
                     |"""


def p_method_body(p):
    """method_body : classStatement
                   | classStatement return_form
                   | return_form
                   | classStatement BREAK SEMICOLON
                   | classStatement method_body
    """


def p_return_form(p):
    """
    return_form : RETURN values SEMICOLON
                | RETURN access_method_object SEMICOLON
                | RETURN SEMICOLON
                | RETURN expression SEMICOLON
                | RETURN string_special_function SEMICOLON
                | RETURN array_special_function_structure SEMICOLON
    """


def p_classStatement(p):
    """classStatement : sentence
                      | access_method_object SEMICOLON"""





# Regla para los errores de sintáxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}' \n'{p}'")
    else:
        print("Error de sintaxis: Fin de archivo inesperado")

# FIN DE APORTACIÓN KEVIN ROLDAN

# Creamos el parser
parser = yacc.yacc()

parser.error = 0

algorith_Roldan = '''<?php
interface StringOperationsInterface {
    public function concatenateStrings($str1, $str2);
    public function getSubstring($str, $start, $length);
}

// Clase StringManipulator que implementa la interfaz
class StringManipulator implements StringOperationsInterface {
    // Función para concatenar dos cadenas
    public function concatenateStrings($str1, $str2) {
        return $str1 + $str2;
    }

    // Función para obtener una subcadena de una cadena
    public function getSubstring($str, $start, $length) {
        return substr($str, $start, $length);
    }
}

// Función flecha fuera de la clase para calcular el cuadrado de un número
$square = fn($number) => $number * $number;

echo "¡Bienvenido al programa!\n";

// Crear una instancia de la clase StringManipulator
$stringManipulator = new StringManipulator();

// // Entrada de texto usando readline y Operaciones de cadena
$string1 = readline("Ingresa la primera cadena: ");
$string2 = readline("Ingresa la segunda cadena: ");
$resultConcatenation = $stringManipulator->concatenateStrings($string1, $string2);
echo "Concatenación de cadenas: $resultConcatenation\n";

$subString = readline("Ingresa una cadena para obtener una subcadena: ");
$start = readline("Ingresa la posición de inicio: ");
$length = readline("Ingresa la longitud de la subcadena: ");
$resultSubstring = $stringManipulator->getSubstring($subString, $start, $length);
echo "Subcadena: $resultSubstring\n";

// Uso de la función flecha
$numToSquare = readline("Ingresa un número para calcular su cuadrado: ");
$userNum = readline("Ingresa un número que usted cree q es el cuadrado del anterior: ");
if ($userNum == $resultSquare) {
    echo "¡Correcto! Has acertado. ¡Bien hecho!\n";
} else {
   $resultSquare = $square($numToSquare);
    echo "Lo siento, la estimación es incorrecta. El cuadrado es: $resultSquare\n";
}

print "Ahora validaremos una expresion booleana con coerción de tipos ";
// Definir una constante booleana
define("MI_CONSTANTE_BOOL", true);

// Expresión booleana con una cadena
$cadena =  readline("Ingrese la cadena a validar con True");
$resultado = $cadena && MI_CONSTANTE_BOOL;

// Verificar el resultado
if ($resultado) {
    echo "La expresión es verdadera.\n";
} else {
    echo "La expresión es falsa.\n";
}
?>
'''

algorith_Poveda = '''
<?php
// Declaración de variables en diferentes representaciones
$decimalNumber = 15; // Representación decimal
$hexNumber = 0x1F; // Representación hexadecimal
$octalNumber = 037; // Representación octal

/*
Comentario multilinea:
Este programa utiliza estructuras de control anidadas
con while y condiciones que involucran AND, OR y XOR.
*/

// Estructura de control: while anidada
while ($decimalNumber <= 20) {
    echo "Número decimal: $decimalNumber";

    // Estructura de control: if anidada con AND y OR
    if (($decimalNumber % 2 == 0) and ($decimalNumber > 10)) {
        echo "El número es par y mayor que 10.";
    } elseif (($decimalNumber % 3 == 0) or ($decimalNumber < 5)) {
        echo "El número es divisible por 3 o menor que 5.";
    } else {
        echo "El número no cumple ninguna de las condiciones especificadas.";
    }

    // Incrementar el número decimal
    $decimalNumber++;

    // Estructura de control: while anidada
    while ($hexNumber > 0) {
        echo "Número hexadecimal: $hexNumber";

        // Estructura de control: if dentro del while anidado con XOR
        if (($octalNumber % 4 == 0) xor ($octalNumber < 10)) {
            echo "El número octal $octalNumber cumple con una de las condiciones.";
        } else {
            echo "El número octal $octalNumber no".4."cumple ninguna o cumple ambas condiciones.";
        }

        // Decrementar el número hexadecimal
        $hexNumber--;
        // Incrementar el número octal
        $octalNumber++;
    }
}
?>
'''

algorith_Mawyin = '''
<?php
class Estudiante {
    public $nombre;
    public $edad;
    public $notas;
    public function construct($nombre, $edad, $notas) {
        $nombre = $nombre;
        $edad = $edad;
        $notas = $notas;
    }
    public function obtenerPromedio() {
        $suma = array_sum($notas);
        $cantidad = count($notas);
        return $suma / $cantidad;
    }  
}
//Creacion de arrays simples de notas
$arregloNotas1 = array(85, 90, 78);
$arregloNotas2 = array(90, 92, 88);
$arregloNotas3 = array(82, 88, 90);
//Creacion de arrays simples de objetos tipo estudiante
$estudiantes = array(
    new Estudiante("Juan", 20, $arregloNotas1),
    new Estudiante("Maria", 22, $arregloNotas2),
    new Estudiante("Pedro", 21, $arregloNotas3)
);
// Imprimir la información de cada estudiante y su promedio de notas usando la estructura for
for ($i = 0; $i < count($estudiantes); $i++) {
    echo "Nombre: " . $estudiantes[$i]->nombre . "<br>";
    echo "Edad: " . $estudiantes[$i]->edad . "<br>";
    echo "Promedio de notas: " . $estudiantes[$i]->obtenerPromedio() . "<br>";
    echo "<br>";
}
// Encontrar el estudiante con el promedio de notas más alto indexando el arreglo estudiantes
$mejorEstudiante = $estudiantes[0];
for ($i = 1; $i < count($estudiantes); $i++) {
    $promedioActual = $estudiantes[$i]->obtenerPromedio();
    $mejorPromedio = $mejorEstudiante->obtenerPromedio();
    if ( $promedioActual > $mejorPromedio ) {
        $mejorEstudiante = $estudiantes[$i];
    }
}
echo "El mejor estudiante del array es: " .  $mejorEstudiante->nombre . "<br>";
// Encontrar el estudiante con la edad más alta
$estudianteMayor = $estudiantes[0];
for ($i = 1; $i < count($estudiantes); $i++) {
    $estudianteActual = $estudiantes[$i]->edad;
    $edadEstudianteMayor = $estudianteMayor->edad;
    if ($estudianteActual > $edadEstudianteMayor) {
        $estudianteMayor = $estudiantes[$i];
    }
}
echo "El  estudiante con mayor edad del array es: " .  $estudianteMayor->nombre . "<br>";
// Encontrar el estudiante con edad igual o superior a una edad establecida
$edadEstablecida = 14 + "12";
$estudianteEdadIgual = $estudiantes[0];
for ($i = 1; $i < count($estudiantes); $i++) {
    $estudianteActual = $estudiantes[$i]->edad;
    $EdadestudianteIgual = $estudianteEdadIgual->edad;
    if ($estudianteActual > $EdadestudianteIgual) {
        $EdadestudianteIgual = $estudiantes[$i];
    }
}
echo "El estudiante con la edad igual a $edadEstablecida es: " .  $EdadestudianteIgual->nombre . "<br>";
//Usando la funcion pop para los arreglos
$ultimoEstudiante = array_pop($estudiantes);
echo "El último estudiante eliminado del array es: " . $ultimoEstudiante->nombre . "<br>";
?>
'''
#parser.parse(algorith_Roldan)
parser.parse(algorith_Poveda)
#parser.parse(algorith_Mawyin)
