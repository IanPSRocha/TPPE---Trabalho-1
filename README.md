# TPPE - Trabalho 1

Repositório destinado a documentar e elaborar a entrega do [primeiro trabalho da disciplina TPPE](https://github.com/andrelanna/fga0242/tree/master/tp1) no 1 semestre de 2023.

### Participantes

| Aluno                                 | Github                                               | Matrícula |
|---------------------------------------|------------------------------------------------------|-----------|
| Ian Pereira de Sousa Rocha            | [@IanPSRocha](https://github.com/IanPSRocha)         | 160124778 |
| João Victor Max Bisinotti de Oliveira | [@joaobisi](https://github.com/joaobisi)             | 170069991 |
| luiz Gustavo Dias Paes Pinheiro       | [@PinheiroLG](https://github.com/PinheiroLG)         | 140169784 |
| Vinicius Edwardo Pereira Oliveira     | [@viniciused26](https://github.com/viniciused26)     | 160147816 |
| Paulo Henrique Costa Gontijo          | [@paulohgontijoo](https://github.com/paulohgontijoo) | 150143800 |
| André Goretti Motta                   | [@AGoretti](https://github.com/AGoretti)             | 160112028 |

## Instalação

Linguagem: Python3 <br>
Para rodar o projeto é nescessário instalar o "parameterized". Para isso rode o comando com "pip3".

>pip3 install parameterized

Para rodar o programa:

>python3 main.py

Para rodar os testes:

>python3 -m unittest completude_test.py

***
# Trabalho Prático 2 da disciplina Técnicas de Programação para Plataformas Emergentes

### Participantes

| Aluno                                 | Github                                               | Matrícula |
|---------------------------------------|------------------------------------------------------|-----------|
| Ian Pereira de Sousa Rocha            | [@IanPSRocha](https://github.com/IanPSRocha)         | 160124778 |
| João Victor Max Bisinotti de Oliveira | [@joaobisi](https://github.com/joaobisi)             | 170069991 |
| luiz Gustavo Dias Paes Pinheiro       | [@PinheiroLG](https://github.com/PinheiroLG)         | 140169784 |
| Vinicius Edwardo Pereira Oliveira     | [@viniciused26](https://github.com/viniciused26)     | 160147816 |
| Paulo Henrique Costa Gontijo          | [@paulohgontijoo](https://github.com/paulohgontijoo) | 150143800 |
| André Goretti Motta                   | [@AGoretti](https://github.com/AGoretti)             | 160112028 |
  
Este trabalho é o Trabalho 2 da disciplina de Técnicas de programação para Plataformas Emergentes, primeiro semestre de 2023 e tem como propósito analisar e explorar cinco das nove características essenciais de um projeto de software de qualidade mencionadas por Fowler. A seguir, serão apresentadas de forma concisa as cinco características escolhidas para análise detalhada.

* Boa documentação;
* Extensibilidade;
* Ausência de duplicidade no código;
* Simplicidade
* Modularidade (baixo acoplamento e alta coesão)

***
## Boa documentação

### 1. Descrição
A documentação de um projeto de software desempenha um papel fundamental em sua sustentabilidade a longo prazo. Ela atua como um manual detalhado e compreensível, fornecendo orientações para entender, manter, colaborar e expandir o software. A documentação deve ser concisa, refletindo a simplicidade do projeto em sua clareza, organização e objetividade.

### 2. Efeitos no código:
* **Estrutura:** A presença de uma documentação adequada contribui para uma estrutura de projeto mais organizada e bem definida. Isso ocorre devido à inclusão de elementos como diagramas, fluxos de trabalho e uma visão geral da arquitetura, que auxiliam na compreensão de como os diversos componentes do sistema se inter-relacionam.
Ao apresentar uma visão geral da estrutura, a documentação facilita o entendimento dos relacionamentos entre módulos e partes do código, tornando mais fácil para os desenvolvedores navegarem pelo projeto e localizarem as informações relevantes.
* **Claridade:** A existência de uma documentação clara assegura uma compreensão adequada das funcionalidades, APIs e comportamentos do software. Essa clareza é essencial para evitar ambiguidades e interpretações equivocadas que poderiam resultar em erros de implementação ou uso inadequado. Uma documentação precisa e abrangente é um fator crucial para garantir que todos os aspectos do software sejam corretamente entendidos e utilizados.
* **Coesão:** A documentação adequada desempenha um papel crucial na promoção da coesão dentro de um projeto de software. Ao fornecer uma documentação clara e abrangente dos componentes, suas finalidades e responsabilidades ficam nitidamente estabelecidas. Isso incentiva os desenvolvedores a aderirem ao princípio de "alta coesão", onde cada módulo possui uma função específica e bem definida, resultando em uma redução do acoplamento entre diferentes partes do código. Aprimorar a coesão geralmente leva a um código mais organizado e de fácil manutenção, pois as responsabilidades são distribuídas de maneira mais eficiente. Isso significa que cada componente possui um propósito claro e contribui de forma significativa para o funcionamento do sistema como um todo. Com uma documentação adequada, os desenvolvedores podem entender facilmente a finalidade de cada componente e como eles se relacionam entre si, resultando em um código mais coeso e sustentável ao longo do tempo.
* **Acoplamento:** A documentação exerce influência sobre o acoplamento, que é a dependência entre as diferentes partes do software. Quanto mais clara e detalhada a documentação, mais fácil se torna compreender a interação entre os módulos. Ao compreender os pontos de acoplamento, os desenvolvedores podem tomar decisões embasadas para reduzir o acoplamento indesejado e promover um design mais flexível e modular. Ademais, a documentação que descreve os requisitos de interface e os contratos entre os módulos desempenha um papel crucial na prevenção de problemas de compatibilidade e alterações incompatíveis decorrentes de mudanças não documentadas. Isso significa que a documentação clara e precisa estabelece diretrizes que ajudam a evitar conflitos e asseguram que as mudanças realizadas no software sejam compatíveis e não prejudiquem o funcionamento adequado do sistema como um todo.

### 3. Relação com os maus cheiros definidos por Fowler:
Uma documentação de qualidade desempenha um papel fundamental na identificação, prevenção e correção de maus cheiros de código. Os maus cheiros de código são indícios de problemas potenciais no design e implementação do software, sugerindo a necessidade de refatoração. É possível observar que, quando a documentação é insuficiente, os programadores tendem a preencher essa lacuna com comentários excessivos no código, na tentativa de explicar partes complexas ou obscuras. No entanto, esses comentários podem se tornar rapidamente obsoletos e não refletir mais o estado atual do código, resultando em informações incorretas. Uma documentação de qualidade fornece explicações claras e detalhadas, diminuindo a necessidade de comentários excessivos e aprimorando a compreensão global do código. Além disso, a falta de uma documentação adequada pode levar à criação de métodos ou classes excessivamente complexos, uma vez que não há uma visão clara dos objetivos de cada elemento. Com uma documentação completa, é mais fácil identificar métodos ou classes com complexidade desnecessária, permitindo que os desenvolvedores simplifiquem a lógica, dividam tarefas complexas em etapas mais simples e, assim, melhorem a legibilidade do código. Dessa forma, a documentação atua como uma ferramenta valiosa para melhorar a qualidade e a manutenibilidade do software.

### 4. Exemplo de operação de refatoração capaz de levar o projeto de código e ter uma boa documentação:
A técnica conhecida como "Extração de Método" envolve a criação de um novo método a partir de um trecho de código existente, onde a lógica relacionada é agrupada em uma única função com um nome significativo. Essa prática não apenas aprimora a clareza e legibilidade do código, mas também tem um impacto positivo na qualidade da documentação do projeto. A extração de método facilita a compreensão do propósito e funcionamento da função para outros desenvolvedores, promovendo uma colaboração mais efetiva no projeto e auxiliando na manutenção futura. Além disso, ao utilizar nomes adequados para métodos e argumentos, a documentação se torna mais legível, simplificando a compreensão do código e evitando a necessidade de comentários excessivos. Essa abordagem contribui para a melhoria geral da documentação, tornando-a mais eficiente e eficaz na comunicação das funcionalidades do software.

***
## Extensibilidade

### 1. Descrição:

A extensibilidade de software é a capacidade de um sistema ou componente ser facilmente estendido ou modificado sem que sejam necessárias mudanças significativas em sua estrutura subjacente. Essa característica permite adicionar novos recursos ou funcionalidades ao software de forma simples, sem comprometer o funcionamento existente. Para alcançar a extensibilidade, é importante aplicar princípios como o Princípio Aberto/Fechado, que torna as entidades abertas para extensão, mas fechadas para modificação, e o Princípio da Inversão de Dependência, que promove baixo acoplamento e dependências invertidas. Essas abordagens, juntamente com padrões de design adequados, contribuem para a criação de sistemas flexíveis e fáceis de estender, permitindo a adaptação às necessidades em constante evolução do software.

### 2. Efeitos no código:

* **Modularidade**: Um código extensível geralmente é composto por módulos bem definidos, cada um responsável por uma funcionalidade específica. Isso resulta em uma estrutura mais organizada, facilitando a compreensão e manutenção do software.
* **Abstração**: A extensibilidade muitas vezes envolve a criação de abstrações, como interfaces ou classes abstratas, que definem contratos para a extensão do sistema. Essas abstrações fornecem uma camada de isolamento entre o código existente e as futuras extensões, permitindo que diferentes implementações sejam adicionadas sem afetar o restante do código.
* **Baixo acoplamento**: A extensibilidade promove o baixo acoplamento entre os componentes do sistema. Isso significa que as dependências entre os módulos são minimizadas, tornando as mudanças e adições mais isoladas. Dessa forma, é possível estender o software sem afetar negativamente outras partes do código.
* **Flexibilidade**: A extensibilidade permite que novos recursos ou funcionalidades sejam adicionados ao software de forma flexível. Isso significa que o código pode ser adaptado para atender às necessidades em constante evolução do sistema, sem exigir grandes reestruturações ou modificações extensivas.
Reutilização: Ao criar um código extensível, é possível promover a reutilização de componentes existentes. Por meio da definição clara de interfaces e abstrações, as implementações podem ser substituídas ou estendidas com relativa facilidade, permitindo que partes do código sejam reaproveitadas em diferentes contextos.
* **Facilidade de manutenção**: Um código extensível tende a ser mais fácil de manter ao longo do tempo. As modificações ou adições de funcionalidades podem ser realizadas de forma mais direta e segura, reduzindo a chance de introduzir erros ou efeitos colaterais indesejados.

### 3. Relação com os maus cheiros definidos por Fowler:

A extensibilidade do software está diretamente relacionada aos maus cheiros de código identificados por Martin Fowler. Maus cheiros como código duplicado, acoplamento excessivo, complexidade excessiva e dependências indevidas têm um impacto negativo na extensibilidade. O código duplicado dificulta a adição de funcionalidades, exigindo modificações em várias partes do código. O alto acoplamento entre componentes dificulta a extensão, pois as alterações em um componente podem afetar outros, exigindo modificações em cascata. A complexidade excessiva torna difícil identificar os pontos de extensão adequados, enquanto dependências indevidas podem aumentar a complexidade das modificações. Ao eliminar esses maus cheiros, aplicando boas práticas de design, é possível criar um código mais limpo, modular e flexível, favorecendo a adição de funcionalidades e a manutenção do software a longo prazo.

### 4. Exemplo de operação de refatoração capaz de levar o projeto de código e ter uma boa Extensibilidade

Uma operação de refatoração que pode contribuir para melhorar a extensibilidade de um projeto de código é a extração de métodos ou funções. Essa técnica envolve identificar trechos de código repetidos ou complexos e transformá-los em métodos separados e bem nomeados.

Ao extrair um método, estamos dividindo o código em unidades lógicas menores e mais coesas. Isso tem vários benefícios para a extensibilidade. Primeiro, reduz a duplicação de código, pois o método extraído pode ser reutilizado em várias partes do sistema. Dessa forma, qualquer modificação ou melhoria no comportamento desse trecho de código pode ser aplicada em um único lugar, facilitando a manutenção e evitando erros introduzidos por alterações inconsistentes.

Além disso, a extração de métodos melhora a modularidade do código, permitindo que cada método tenha uma única responsabilidade clara. Isso ajuda a reduzir o acoplamento entre as diferentes partes do sistema, tornando-o mais flexível para adicionar novas funcionalidades. Os métodos extraídos também podem servir como pontos de extensão, onde novos comportamentos podem ser adicionados de forma coesa e sem afetar o código existente.

***
## Ausência de duplicidades

### 1. Descrição
A ausência de duplicidades é uma característica desejável em código de qualidade, e ela se refere ao princípio de evitar repetições desnecessárias de trechos de código. Quando uma duplicidade é identificada no código, significa que um mesmo trecho de lógica, expressão ou funcionalidade está repetido em mais de um lugar. Isso pode ocorrer em funções, classes ou até mesmo em trechos menores de código.

### 2. Efeitos no código:
* **Estrutura:** A ausência de duplicidades melhora a estrutura do código, pois evita a fragmentação de lógica em vários lugares e promove uma organização mais coesa e concisa.
* **Claridade:** O código fica mais claro e fácil de entender quando duplicações são eliminadas, uma vez que os desenvolvedores não precisam procurar e entender múltiplas ocorrências de uma mesma lógica.
* **Eficiência:** A reutilização de código reduz o tamanho do programa, levando a um código mais enxuto e fácil de manter.
* **Manutenção:** Quando uma mudança é necessária, a ausência de duplicidades implica em fazer a alteração em um único lugar, aumentando a produtividade e diminuindo a probabilidade de erros.
* **Coesão:** A ausência de duplicidades fortalece a coesão do código, pois concentra a lógica em um único local, tornando o comportamento de uma função ou classe mais consistente.
* **Acoplamento:** A redução de duplicações também pode levar a um menor acoplamento entre diferentes partes do código, uma vez que a funcionalidade compartilhada é movida para um local central.

### 3. Relação com os maus cheiros definidos por Fowler:
Entre os maus cheiros de código definidos por Martin Fowler, a ausência de duplicidades está diretamente relacionada ao "Duplicated Code" (Código Duplicado). Esse mau cheiro ocorre quando há repetição de trechos de código em locais diferentes do projeto. O "Código Duplicado" é considerado um problema porque dificulta a manutenção, torna o código mais propenso a erros e pode levar a inconsistências.

### 4. Exemplo de operação de refatoração capaz de levar o projeto de código e ter uma boa documentação:
A operação de refatoração que pode ser aplicada para eliminar duplicidades e alcançar a característica desejada é a extração de método ou função. Essa técnica consiste em identificar trechos de código duplicados e movê-los para uma nova função ou método que possa ser chamado em todas as ocorrências onde a duplicação existia.

Passos para a refatoração:

* **Identificação:** Localize trechos de código repetidos em diferentes partes do projeto.
* **Criação da função ou método:** Crie uma nova função ou método que contenha o trecho de código duplicado. Essa função deve ser genérica o suficiente para ser reutilizada em todos os locais onde a duplicação foi encontrada.
* **Substituição:** Substitua todas as ocorrências duplicadas pelo chamado da nova função ou método criado no passo anterior.
* **Testes:** Certifique-se de que todas as funcionalidades afetadas pelos ajustes estão funcionando corretamente e que os testes continuam passando.
* **Validação:** Verifique se a eliminação das duplicidades não causou nenhum efeito colateral indesejado no restante do código.

Após a conclusão desses passos, o código deve estar livre de duplicidades, melhorando sua estrutura, claridade, coesão e possivelmente reduzindo acoplamento, tornando-o mais limpo e mais fácil de manter.

Outro benefício é que a extração de métodos ajuda a reduzir a complexidade do código. Ao dividir o código em partes menores e bem definidas, fica mais fácil entender e dar manutenção, tornando as futuras extensões mais simples e menos propensas a introduzir bugs.

No entanto, é importante ter cuidado ao extrair métodos. É necessário considerar a coesão, garantindo que cada método tenha uma única responsabilidade bem definida. Também é fundamental garantir que os parâmetros e retornos dos métodos extraídos sejam adequados e bem documentados.

***
## Simplicidade

### 1. Descrição
A simplicidade em um bom projeto de software significa criar soluções claras e fáceis de entender, evitando complexidades desnecessárias. Isso resulta em código estruturado e organizado, facilitando a leitura e compreensão por desenvolvedores, além de reduzir a duplicação de código. A busca pela simplicidade também melhora a coesão entre os componentes do software, define responsabilidades precisas e separadas, e diminui o acoplamento entre os módulos, tornando o código mais flexível. Além disso, um código simples é mais fácil de testar e depurar, acelerando a manutenção e identificação de erros. A simplicidade também beneficia a integração de novos membros da equipe, aumenta a colaboração e pode resultar em melhor desempenho do software. No entanto, é importante equilibrar a simplicidade com a funcionalidade necessária para garantir a qualidade do produto final.

### 2. Efeitos no Código
* **Estrutura clara e organizada:** A simplicidade geralmente resulta em uma estrutura de código mais clara e bem organizada. A lógica do programa é mais fácil de entender e seguir, facilitando a navegação pelo código-fonte.
* **Facilidade de leitura e compreensão:** Um código simples é mais legível, o que significa que outros desenvolvedores podem compreendê-lo com mais facilidade. Isso é especialmente importante em projetos de equipe, onde diferentes pessoas podem trabalhar em partes diferentes do código.
* **Redução da duplicação de código:** A busca pela simplicidade pode levar a identificar oportunidades de reutilização de código, reduzindo assim a duplicação. Isso torna o código mais conciso, mais fácil de manter e menos propenso a erros.
* **Coesão melhorada:** A simplicidade muitas vezes leva a um maior grau de coesão entre os componentes do software. As responsabilidades de cada módulo ficam mais bem definidas e separadas, facilitando a manutenção e modificação.
* **Baixo acoplamento:** A simplicidade geralmente leva a um menor acoplamento entre os módulos do software. Com menos dependências complexas, é mais fácil alterar um componente específico sem afetar todo o sistema, tornando o código mais flexível e adaptável.
* **Facilidade de testes:** Um código simples é mais fácil de testar, pois as funcionalidades estão bem definidas e isoladas. Isso torna os testes de unidade e integração mais simples e eficazes.
* **Facilidade de depuração:** Em um código simples, é mais fácil identificar a origem dos bugs e problemas, pois a lógica é mais clara e a quantidade de elementos que podem causar erros é reduzida.
* **Facilidade de manutenção e evolução:** A simplicidade torna a manutenção e evolução do software mais eficientes. Novas funcionalidades podem ser implementadas de forma mais rápida e menos propensa a criar problemas inesperados.

### 3. Relação com os maus cheiros definidos por Fowler:
A característica da simplicidade em um código de software está diretamente relacionada à resolução de diversos "maus cheiros" identificados por Martin Fowler. Ao buscar a simplicidade no código, muitos desses problemas são naturalmente mitigados ou eliminados. Aqui estão algumas das relações entre a simplicidade e alguns "maus cheiros" específicos definidos por Fowler:

* **Duplicação de código (Duplicated Code)**
* **Métodos longos (Long Method)**
* **Classes grandes (Large Class)**
* **Muitos parâmetros (Long Parameter List)**
* **Métodos complexos condicionais (Complex Conditional Expressions)**
* **Dependências desnecessárias (Inappropriate Intimacy)**
* **Código pouco claro (Shotgun Surgery)**
* **Comentários desnecessários (Comments)**
* **Classes com muitas responsabilidades (Large Class)**

### 4. Exemplo de operação de refatoração capaz de levar o projeto de código a ter uma boa simplicidade:
Um exemplo de operação de refatoração que pode levar o projeto de código a ter uma boa simplicidade é a extração de método (Extract Method) na qual é uma técnica de refatoração que consiste em identificar trechos de código dentro de um método que realizam uma tarefa específica e isolá-los em um novo método. Essa operação tem como objetivo melhorar a legibilidade, reutilização e manutenção do código.
Quando um método se torna muito longo, possui trechos repetidos ou executa várias tarefas distintas, pode ser difícil compreender sua funcionalidade como um todo. Além disso, a repetição de código em vários lugares aumenta a probabilidade de erros e dificulta a atualização do software, caso a lógica precise ser modificada.
Ao aplicar a extração de método, o trecho de código relevante é isolado em um novo método separado, com um nome descritivo que indique sua finalidade. Os parâmetros necessários para a execução do trecho de código são passados para o novo método, e ele pode retornar um valor, se for o caso. Assim, o método original passa a chamar o novo método, delegando a responsabilidade pela tarefa específica.

***
## Modularidade (Baixo Acoplamento e Alta Coesão)

### 1. **Descrição:**
A modularidade é uma característica essencial em projetos de software que se refere à divisão do código em módulos independentes e bem definidos. Esses módulos devem ser altamente coesos, ou seja, cada módulo deve ter uma única responsabilidade bem definida, com suas funcionalidades relacionadas e organizadas de forma lógica e coesa. Além disso, os módulos devem ser fracos ou pouco acoplados, o que significa que as dependências entre os módulos devem ser minimizadas, reduzindo a interdependência entre eles.

### 2. **Efeitos no Código:**
- **Estrutura:** A modularidade contribui para uma estrutura clara e organizada do código, facilitando a leitura, manutenção e entendimento.
- **Claridade:** Módulos coesos e com baixo acoplamento tornam o código mais legível e compreensível, pois cada parte é mais específica e focada em sua funcionalidade.
- **Coesão:** A alta coesão permite que o código seja mais coeso, ou seja, cada módulo contém um conjunto relacionado de funcionalidades, o que ajuda a evitar fragmentação e dispersão de lógica.
- **Acoplamento:** Com baixo acoplamento, as mudanças em um módulo têm menos impacto em outros módulos, tornando o código mais flexível e menos propenso a efeitos colaterais não intencionais.
- **Reusabilidade:** Módulos bem definidos e independentes são mais fáceis de serem reutilizados em diferentes partes do código ou até mesmo em outros projetos.

### 3. **Relação com Maus-Cheiros de Código:**
- **Feature Envy (Inveja de Funcionalidade):** Esse mau cheiro ocorre quando um módulo ou classe usa excessivamente os métodos de outra classe, demonstrando acoplamento excessivo. Isso pode ser um indicativo de que a funcionalidade deveria estar em um módulo diferente, mais coeso e com baixo acoplamento.
- **Divergent Change (Mudança Divergente):** Acontece quando uma classe ou módulo é frequentemente modificado por motivos distintos. Isso pode indicar falta de coesão e que o módulo deveria ser dividido em partes mais especializadas e independentes.
- **Shotgun Surgery (Cirurgia de Escopeta):** Ocorre quando uma única mudança no código requer várias alterações em diferentes partes do sistema. Isso pode ser um indício de alto acoplamento entre os módulos e que as responsabilidades não estão bem distribuídas.

### 4. **Operação de Refatoração:**
**Extrair Classe (Extract Class):** Essa operação permite extrair parte da funcionalidade de uma classe existente em uma nova classe separada. Essa refatoração é útil quando uma classe tem responsabilidades que não pertencem totalmente a ela e devem ser colocadas em uma nova unidade coesa e com baixo acoplamento.

Para aplicar essa operação de refatoração, siga os seguintes passos:

1. Identifique parte da funcionalidade da classe que pode ser agrupada em uma nova classe com responsabilidades mais específicas.
2. Crie uma nova classe e mova os métodos e atributos relacionados a essa funcionalidade para a nova classe.
3. Caso necessário, ajuste as dependências entre as classes para garantir o baixo acoplamento.
4. Verifique se o comportamento externamente observável da classe original não foi alterado e que o sistema continua funcionando corretamente após a extração.

Ao extrair classes coesas e com baixo acoplamento, você estará promovendo a modularidade do código, melhorando sua manutenibilidade, legibilidade e reusabilidade.
