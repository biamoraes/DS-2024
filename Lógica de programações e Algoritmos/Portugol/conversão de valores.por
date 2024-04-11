programa
{
	
	funcao inicio(){
	real tx, moeda, resultado
	inteiro opcao
	
		escreva("Qual a cotação do dolar?")
		leia(tx)

          escreva("Escolha: \n")
          escreva("[1] - Converter Real para Dolar \n")
          escreva("[2] - Converter Dolar para Real \n")

          escreva("Digite um numero para conversao: ")
          leia(moeda)

          se(moeda == 1){
          escreva("Qual o valor em dolar a ser convertido para real?")
          leia(moeda)
          resultado = moeda * tx
          
          }senao {

           
          
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 567; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */