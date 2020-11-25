# Introdução

Este script simula o funcionamento da applet GbAs, que até recentemente era utilizada por diversos bancos brasileiros. O objetivo deste script era permitir que o site dos bancos fosse utilizado mesmo por usuários que não pudessem ou não quisessem instalar o suporte a applets Java em seus navegadores, devido às implicações que esse plugin gerava para a segurança do próprio usuário.

O OperaGbAs existe desde 2010, porém até o momento não havia sido divulgado publicamente por um simples motivo: eu o utilizava diariamente, e queria evitar a dor de cabeça de ter que ficar atualizando o código do script caso a fabricante do módulo de segurança quisesse impedir o uso da minha solução alternativa.

Com a descontinuação do suporte a NPAPI pelo Firefox, os bancos [passarão a adotar o Warsaw](https://archive.is/j6Zam), um *daemon* que executa como superusuário na máquina do correntista. Desta forma, não será mais possível utilizar o script, porém acredito que este contenha informações historicamente relevantes para pessoas que estudem ou se interessem por segurança da informação.


# Conteúdo do repositório

 * [operagbas.js](operagbas.js): arquivo a ser instalado como userscript no Opera (versões com engine Presto).
 * [gbasConfig.py](gbasConfig.py): calcula o ID único da máquina a partir de uma instalação do GbAs oficial (desculpe, Python 2).


# Por que Opera?

Na época, o Opera ainda não era baseado na engine Blink. Ele tinha a sua própria engine, e o mecanismo que ele disponibilizava para a escrita de userscripts era mais completo que o de outros navegadores. Em particular, ele permitia ao userscript agir antes dos elementos da página serem carregados. Isso me dava mais segurança de que o script não seria detectado pelo banco e eles não bloqueariam minha conta pensando que alguém estava tentando fraudá-la.

Em dado momento, cheguei a implementar uma versão que funcionava como extensão de Firefox, mas abandonei o projeto.


# Vulnerabilidade de 2010 do GbAs

Enquanto eu fazia a engenharia reversa no GbAs, acabei encontrando uma vulnerabilidade de RCE, reforçando minhas suspeitas de que não era seguro usar o plugin de "segurança".

Essa vulnerabilidade foi apresentada na palestra *Insegurança em módulos de segurança bancários: brechas permitem invasão de computadores de correntistas*, proferida durante a edição de 2010 do [H2HC - Hackers to Hackers Conference](http://www.h2hc.com.br).

O repositório [h2hc-2010-gbas-rce](https://github.com/thotypous/h2hc-2010-gbas-rce) contém a apresentação e os vídeos e códigos de demonstração do exploit.

