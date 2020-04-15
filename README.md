## Introdução
Módulo Python utilizado para criação de uma estrutura aleatória de diretórios e arquivos, em formato árvore.
```sh
$ tree
.
├── 22b3e01b3d101a013916a3b6ae7597ef
├── 2abb1575a911e02103a9b3a5a726d18c
│   ├── 61c1d8908014952c95c1b027639f0bef
│   │   ├── 13361b4d995d3caa7fb9ace55fc9a3d6
│   │   │   └── ffba85c2105c9b4d72912d1ab43aa4a7
│   │   ├── 23d03c00fdf558cf95f007236cec15b6
│   │   ├── 2c4d0fe848b76ec0e979b8595aa1a1e6
│   │   ├── 4d5af581d1b75b35483d9d3a4186ec4b
```

Os nomes dos diretórios e arquivos são gerados sempre utilizando um hash MD5 para evitar conflitos de nomes.

## Pré Requisitos

### Listagem dos Pré Requisitos
* Sistema operacional [Unix](https://pt.wikipedia.org/wiki/Unix)
* [python](https://www.python.org/download/releases/3.0/) - acima da versão 3.6
    * [Módulo PyYaml](https://pypi.org/project/PyYAML/) - acima da versão 5.3

### Instalação das Dependências
Para instalação do PyYaml utilizaremos o gerenciador de pacotes [PIP3](https://pip.pypa.io/en/stable/):
```sh 
pip3 install PyYaml
```
Ou simplesmente importaremos o [arquivo](https://github.com/lbmello/random-tree-generator/blob/master/requirements.txt) que configura o ambiente:
```sh 
pip3 install -r requirements.txt
```

## Config.YAML
Arquivo de configuração onde os parâmetros para criação da árvore de diretórios/arquivos são definidos.

Sua localização padrão é na raiz do projeto, sempre com nome 'config.yaml'.

```yaml
- basic:
    path: '/tmp/testetree'
    levels: 8
    size: 2
    debug: True
```

### Campos do arquivo Config.YAML
- path: (string) - Local aonde o conteúdo da árvore será gerado.

- levels: (inteiro) - Quantidade de subpastas, contando da raiz.

- size: (inteiro) - Multiplicador de tamanho da árvore. O número definido neste campo será multiplicado por uma constante e o resultado será usado para definir o alcance da função randômica que cria as pastas e os arquivos. Quando maior for o {size}, mais pastas e arquivos serão gerados. Independente da quantidade de níveis. 
    Para o alcance dos arquivos defini-se (size * {3}), para as pastas (size * {2}).
    Ex. Se o size for definido no arquivo de conf como 3, durante a execução do programa, poderão ser geradas de 1 até 9 arquivos por pasta, pois para arquivos defini-se size*3.

- debug: (booleano) - Se marcado como True, exibe em shell alguns status durante a execução.

## Execução do Módulo
Após clonar o repositório, configurar as dependências do ambiente e setar os parâmetros personlizados no arquivo de configuração, é necessário apenas executar o módulo:
```sh
$ python3 -m random_tree
```
