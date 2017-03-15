# Introdução

Este script simula o funcionamento da applet GbAs, que até recentemente era utilizada por diversos bancos brasileiros. O objetivo deste script era permitir que o site dos bancos fosse utilizado mesmo por usuários que não pudessem ou não quisessem instalar o suporte a applets Java em seus navegadores, devido às implicações que esse plugin gerava para a segurança do próprio usuário.

O [OperaGbAs](operagbas.js) existe desde 2010, porém até o momento não havia sido divulgado publicamente por um simples motivo: eu o utilizava diariamente, e e queria evitar a dor de cabeça de ter que ficar atualizando o código do script caso a fabricante do módulo de segurança quisesse impedir o uso da minha solução alternativa. 

Com a descontinuação do suporte a NPAPI pelo Firefox, os bancos [passarão a adotar o Warsaw](https://archive.is/j6Zam), um *daemon* que executa como superusuário na máquina do correntista. Desta forma, não será mais possível utilizar o script, porém acredito que este contenha informações historicamente relevantes para pessoas que estudem ou se interessem por segurança da informação.

# Palestra relacionada

Este script foi apresentado ao público, apesar de não ter seu código fonte divulgado naquele momento, na palestra *Insegurança em módulos de            segurança bancários: brechas permitem invasão de computadores
de correntistas*, proferida durante a edição de 2010 do [H2HC - Hackers to Hackers Conference](http://www.h2hc.com.br).

* [Slides](https://pmatias.me/operagbas/2010-h2hc-explorando-applets.pdf) da palestra
* Vídeos do OperaGbAs: [1](https://pmatias.me/operagbas/operagbas-video1.mp4) e [2](https://pmatias.me/operagbas/operagbas-video2.mp4)
* [Vídeo](https://pmatias.me/operagbas/demonstracao-exploit.ogv) do exploit discutido na palestra

