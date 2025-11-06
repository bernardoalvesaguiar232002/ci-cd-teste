O que é CI/CD e por que é importante?

Resposta: CI é a prática de integrar o código frequentemente e testar a cada push. CD, refere-se a automatizar a entrega ou a publicação do software.
Essas práticas são importantes para detectar erros mais cedo, garantir que o código novo se integra bem ao existente e automatizar o processo de entrega.


Em qual pasta os workflows do GitHub ficam armazenados?
Resposta: Os workflows ficam armazenados no diretório .github/workflows dentro do repositório.


O que aparece no log do GitHub Actions após a execução?
Resposta: log mostrará a execução de cada etapa definida no arquivo teste.yml. Na etapa "Executar script", aparecerá a saída do comando python main.py 'Hello CI/CD!'.


O que acontece se alterar o código e fizer novo push?
Resposta: Como o workflow está configurado para rodar no evento push para a branch main, o GitHub Actions detectará automaticamente o novo push e executará todo o pipeline "Teste CI" novamente.


O que acontece se um teste falhar?
Resposta:Se um assert de teste falhar, o comando pytest falhará. Isso fará com que a etapa "Executar testes" no GitHub Actions falhe, e todo o workflow será marcado como "Falho" (com um X vermelho). Isso sinaliza ao desenvolvedor que o push recente quebrou um teste e não deve ser integrado sem antes fazer uma correção.


Como o GitHub Actions ajuda a detectar erros cedo?
Resposta: Ele ajuda ao automatizar a execução de testes em um ambiente limpo toda vez que um desenvolvedor faz um push. Se o novo código introduzir um bug que faça um teste falhar, o desenvolvedor é notificado imediatamente, antes que esse erro chegue a outros desenvolvedores ou à produção.


Quais seriam exemplos reais de CI/CD em projetos web ou mobile?
Resposta:
-Executar testes unitários.
-Fazer o "build" do projeto.
-Fazer o "deploy" automático em um ambiente de testes para revisão.
-Executar testes automatizados.
-Compilar o aplicativo, com arquivo .apk ou .ipa


Como o deploy automático poderia ser feito a partir deste pipeline?
Resposta: O deploy seria feito adicionando novas etapas no arquivo teste.yml, após a etapa de testes:
-Autenticar em um serviço de nuvem como AWS, Azure, Google Cloud.
-Executar comandos para enviar o código atualizado para o servidor ou atualizar um container.