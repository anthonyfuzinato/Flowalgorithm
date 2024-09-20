Algoritmo "Calcular_Media_Combustivel"
// Descrição   : [Com Este progama vais calcular a media de litros a cada 100km
// Autor(a)    : Anthony Fuzinato
// Data atual  : 29-09-2023
Var
// Dados de Entrada
 Kilometragem: real
 Litros: real
//Dados de Saida
 MediaCombustivel: real

Inicio
// input
  escreva ("Escreva a kilometragem percorrida:")
  leia (Kilometragem)
  escreva ("Escreva os litros gastos:")
  leia (Litros)
//processamento
  MediaCombustivel <- 100 * Litros / Kilometragem
//output
  escreva ("Aqui está seu resultado:")
  escreva (MediaCombustivel)
Fimalgoritmo