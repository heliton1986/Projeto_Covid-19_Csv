# Projeto 1 Uniasselvi

## Dados da COVID-19

### Importar bibliotecas necessárias

In [ ]:

```
!conda install pandas -y
```

In [1]:

```
# Biblioteca de dataframes do Python
import pandas as pd

# Biblioteca para análise científica
import numpy as np
```

In [ ]:

```
pd.set_option('display.max_rows', None)
```

In [2]:

```
# Extrair o conteúdo do gz
data = pd.read_csv( 'caso_full.csv.gz', compression='gzip', error_bad_lines=False )
```

### Verificando apenas as 5 primeiras linhas

In [3]:

```
data.head()
```

Out[3]:

|      |       city | city_ibge_code |       date | epidemiological_week | estimated_population | estimated_population_2019 | is_last | is_repeated | last_available_confirmed | last_available_confirmed_per_100k_inhabitants | last_available_date | last_available_death_rate | last_available_deaths | order_for_place | place_type | state | new_confirmed | new_deaths |
| ---: | ---------: | -------------: | ---------: | -------------------: | -------------------: | ------------------------: | ------: | ----------: | -----------------------: | --------------------------------------------: | ------------------: | ------------------------: | --------------------: | --------------: | ---------: | ----: | ------------: | ---------: |
|    0 | Rio Branco |      1200401.0 | 2020-03-17 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        3 |                                       0.72566 |          2020-03-17 |                       0.0 |                     0 |               1 |       city |    AC |             3 |          0 |
|    1 |        NaN |           12.0 | 2020-03-17 |               202012 |             894470.0 |                  881935.0 |   False |       False |                        3 |                                       0.33539 |          2020-03-17 |                       0.0 |                     0 |               1 |      state |    AC |             3 |          0 |
|    2 | Rio Branco |      1200401.0 | 2020-03-18 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        3 |                                       0.72566 |          2020-03-18 |                       0.0 |                     0 |               2 |       city |    AC |             0 |          0 |
|    3 |        NaN |           12.0 | 2020-03-18 |               202012 |             894470.0 |                  881935.0 |   False |       False |                        3 |                                       0.33539 |          2020-03-18 |                       0.0 |                     0 |               2 |      state |    AC |             0 |          0 |
|    4 | Rio Branco |      1200401.0 | 2020-03-19 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        4 |                                       0.96754 |          2020-03-19 |                       0.0 |                     0 |               3 |       city |    AC |             1 |          0 |

## Verificando número de linhas (registros) e colunas (atributos)

In [4]:

```
data.shape
```

Out[4]:

```
(2135152, 18)
```

In [5]:

```
f"O dataframe possui {data.shape[0]} registros e {data.shape[1]} colunas" 
```

Out[5]:

```
'O dataframe possui 2135152 registros e 18 colunas'
```

### Verificando todos atributos (colunas) da tabela

In [6]:

```
list(data.columns) 
```

Out[6]:

```
['city',
 'city_ibge_code',
 'date',
 'epidemiological_week',
 'estimated_population',
 'estimated_population_2019',
 'is_last',
 'is_repeated',
 'last_available_confirmed',
 'last_available_confirmed_per_100k_inhabitants',
 'last_available_date',
 'last_available_death_rate',
 'last_available_deaths',
 'order_for_place',
 'place_type',
 'state',
 'new_confirmed',
 'new_deaths']
```

## Verificar os tipos de dados de cada coluna

In [7]:

```
data.dtypes
```

Out[7]:

```
city                                              object
city_ibge_code                                   float64
date                                              object
epidemiological_week                               int64
estimated_population                             float64
estimated_population_2019                        float64
is_last                                             bool
is_repeated                                         bool
last_available_confirmed                           int64
last_available_confirmed_per_100k_inhabitants    float64
last_available_date                               object
last_available_death_rate                        float64
last_available_deaths                              int64
order_for_place                                    int64
place_type                                        object
state                                             object
new_confirmed                                      int64
new_deaths                                         int64
dtype: object
```

## Convertendo o tipo de dado da coluna 'date' para datetime

In [8]:

```
data['date'] = pd.to_datetime( data['date'] )
```

In [9]:

```
data.dtypes
```

Out[9]:

```
city                                                     object
city_ibge_code                                          float64
date                                             datetime64[ns]
epidemiological_week                                      int64
estimated_population                                    float64
estimated_population_2019                               float64
is_last                                                    bool
is_repeated                                                bool
last_available_confirmed                                  int64
last_available_confirmed_per_100k_inhabitants           float64
last_available_date                                      object
last_available_death_rate                               float64
last_available_deaths                                     int64
order_for_place                                           int64
place_type                                               object
state                                                    object
new_confirmed                                             int64
new_deaths                                                int64
dtype: object
```

In [10]:

```
data.head()
```

Out[10]:

|      |       city | city_ibge_code |       date | epidemiological_week | estimated_population | estimated_population_2019 | is_last | is_repeated | last_available_confirmed | last_available_confirmed_per_100k_inhabitants | last_available_date | last_available_death_rate | last_available_deaths | order_for_place | place_type | state | new_confirmed | new_deaths |
| ---: | ---------: | -------------: | ---------: | -------------------: | -------------------: | ------------------------: | ------: | ----------: | -----------------------: | --------------------------------------------: | ------------------: | ------------------------: | --------------------: | --------------: | ---------: | ----: | ------------: | ---------: |
|    0 | Rio Branco |      1200401.0 | 2020-03-17 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        3 |                                       0.72566 |          2020-03-17 |                       0.0 |                     0 |               1 |       city |    AC |             3 |          0 |
|    1 |        NaN |           12.0 | 2020-03-17 |               202012 |             894470.0 |                  881935.0 |   False |       False |                        3 |                                       0.33539 |          2020-03-17 |                       0.0 |                     0 |               1 |      state |    AC |             3 |          0 |
|    2 | Rio Branco |      1200401.0 | 2020-03-18 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        3 |                                       0.72566 |          2020-03-18 |                       0.0 |                     0 |               2 |       city |    AC |             0 |          0 |
|    3 |        NaN |           12.0 | 2020-03-18 |               202012 |             894470.0 |                  881935.0 |   False |       False |                        3 |                                       0.33539 |          2020-03-18 |                       0.0 |                     0 |               2 |      state |    AC |             0 |          0 |
|    4 | Rio Branco |      1200401.0 | 2020-03-19 |               202012 |             413418.0 |                  407319.0 |   False |       False |                        4 |                                       0.96754 |          2020-03-19 |                       0.0 |                     0 |               3 |       city |    AC |             1 |          0 |

## 1 - Qual a data mais antiga dos casos?

In [11]:

```
data[['date']].sort_values('date', ascending=False)
```

Out[11]:

|         |       date |
| ------: | ---------: |
| 2135151 | 2021-05-25 |
|  922043 | 2021-05-25 |
|  922045 | 2021-05-25 |
|  922046 | 2021-05-25 |
|  922047 | 2021-05-25 |
|     ... |        ... |
| 1831285 | 2020-02-27 |
| 1831284 | 2020-02-26 |
| 1831283 | 2020-02-26 |
| 1831282 | 2020-02-25 |
| 1831281 | 2020-02-25 |

2135152 rows × 1 columns

## 2 - Quantos casos teve no estado de São Paulo

In [12]:

```
data['state'].unique()
```

Out[12]:

```
array(['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG',
       'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR',
       'RS', 'SC', 'SE', 'SP', 'TO'], dtype=object)
```

In [13]:

```
data[data['state'] == 'SP'].shape[0]
```

Out[13]:

```
250941
```

## 3 - Quantos casos apenas na cidade de São Paulo

In [14]:

```
# Primeiramente saber quais são as cidades do estado de São Paulo
# loc
data.loc[data['state'] == "SP", 'city'].unique()
```

Out[14]:

```
array(['São Paulo', nan, 'Santana de Parnaíba', 'Ferraz de Vasconcelos',
       'Carapicuíba', 'Mauá', 'Santo André', 'São Bernardo do Campo',
       'São Caetano do Sul', 'Guarulhos', 'Barueri', 'Campinas', 'Cotia',
       'Jaguariúna', 'Osasco', 'São José do Rio Preto',
       'São José dos Campos', 'Importados/Indefinidos', 'Suzano',
       'Taubaté', 'Vargem Grande Paulista', 'Hortolândia',
       'Mogi das Cruzes', 'Caieiras', 'Embu das Artes', 'Iracemápolis',
       'Jundiaí', 'Poá', 'Ribeirão Pires', 'Rio Claro', 'São Sebastião',
       'Taboão da Serra', 'Valinhos', 'Arujá', 'Louveira', 'Mairiporã',
       'Ribeirão Preto', 'Tatuí', 'Diadema', 'Sorocaba', 'Brodowski',
       'Cajamar', 'Itapevi', 'Itupeva', 'Jandira', 'Paulínia',
       'Penápolis', 'Piracicaba', 'Porto Feliz', 'Santos', 'São Pedro',
       'Americana', 'Araçatuba', 'Bauru', 'Cachoeira Paulista',
       'Franco da Rocha', 'Guarujá', 'Itapecerica da Serra',
       'Itaquaquecetuba', 'Lençóis Paulista', 'Matão', 'Mogi Guaçu',
       'Nova Odessa', 'Pirajuí', 'Salto de Pirapora', 'Santa Isabel',
       'São José do Rio Pardo', 'São Vicente', 'Vinhedo', 'Votorantim',
       'Votuporanga', 'Indaiatuba', 'Itanhaém', 'Limeira', 'Praia Grande',
       'Agudos', 'Araraquara', 'Assis', 'Dracena', 'Franca',
       'Francisco Morato', 'Itararé', 'Itu', 'Jaú', 'Águas de Lindóia',
       'Adamantina', 'Atibaia', 'Cravinhos', 'Jaboticabal', 'Marília',
       'Promissão', 'Botucatu', 'Cedral', 'Guararapes', 'Itapira',
       'José Bonifácio', 'Orlândia', 'Pariquera-Açu', 'Santa Branca',
       'São Manuel', 'Itapetininga', 'Terra Roxa', 'Birigui', 'Boituva',
       'Caraguatatuba', 'Embu-Guaçu', 'Ilha Comprida', 'Mirassol',
       'Presidente Venceslau', 'Santa Cruz do Rio Pardo', 'São Carlos',
       'Araras', 'Barretos', 'Bebedouro', 'Bragança Paulista',
       'Catanduva', 'Ibiúna', 'Itatiba', 'Monte Alto', 'Peruíbe',
       'Pindamonhangaba', 'Rio Grande da Serra', 'Salto', 'Sumaré',
       'São Roque', 'Avaré', 'Bady Bassitt', 'Batatais', 'Caçapava',
       'Guararema', 'Jacareí', 'Jales', 'Joanópolis', 'Laranjal Paulista',
       'Mococa', 'Olímpia', 'Pindorama', 'Presidente Prudente',
       'Sertãozinho', 'Tanabi', 'Artur Nogueira', 'Barra do Turvo',
       'Eldorado', 'Guaratinguetá', 'Ilhabela', 'Itapeva', 'Itatinga',
       'Jaci', 'São João da Boa Vista', 'Araçoiaba da Serra', 'Cubatão',
       'Ourinhos', 'Pedra Bela', 'Porto Ferreira',
       "Santa Bárbara d'Oeste", 'São Miguel Arcanjo', 'Tupã',
       'Águas de São Pedro', 'Amparo', 'Américo Brasiliense',
       'Araçariguama', 'Caiabu', 'Estiva Gerbi', 'Ibirá', 'Santa Lúcia',
       'Jardinópolis', 'Campos do Jordão', 'Garça', 'Igaratá', 'Macatuba',
       'Ubatuba', 'Bariri', 'Cajuru', 'Conchas', 'Leme', 'Lins',
       'Mairinque', 'Mongaguá', 'Nhandeara', 'Pilar do Sul', 'Pontal',
       'Rincão', 'Várzea Paulista', 'Andradina', 'Apiaí', 'Bilac',
       'Buritama', 'Capão Bonito', 'Cruzeiro', 'Fernandópolis',
       'Igarapava', 'Lorena', 'Macedônia', 'Mogi Mirim', 'Monte Mor',
       'Morro Agudo', 'Morungaba', 'Pederneiras', 'Piratininga',
       'Pratânia', 'Rinópolis', 'Alambari', 'Campo Limpo Paulista',
       'Castilho', 'Duartina', 'Fartura', 'Piracaia', 'Santa Gertrudes',
       'São Joaquim da Barra', 'Taiaçu', 'Arandu', 'Ilha Solteira',
       'Juquitiba', 'Mineiros do Tietê', 'Paulistânia', 'Rancharia',
       'Registro', 'Santo Antônio da Alegria', 'Angatuba', 'Aparecida',
       'Avaí', 'Cananéia', 'Iguape', 'Junqueirópolis', 'Piedade',
       'Populina', 'Serrana', 'Taquarituba', 'Tarabai', 'Iepê', 'Piraju',
       'Taquaritinga', 'Elias Fausto', 'Guzolândia', 'Miguelópolis',
       'Mirandópolis', 'Quintana', 'Capela do Alto', 'Chavantes',
       'Nazaré Paulista', 'Quatá', 'São Lourenço da Serra',
       'Vista Alegre do Alto', 'Cabreúva', 'Jaborandi', 'Aguaí',
       'Areiópolis', 'Barrinha', 'Biritiba Mirim', 'Cajati',
       'Espírito Santo do Pinhal', 'Itariri', 'Lucélia', 'Miracatu',
       'Palmital', 'Pirassununga', 'Pitangueiras', 'Salesópolis',
       'Santa Rita do Passa Quatro', 'São Sebastião da Grama',
       'Barra Bonita', 'Borborema', 'Cordeirópolis', 'Dobrada',
       'Engenheiro Coelho', "Estrela d'Oeste", 'Guaíra', 'Itirapina',
       'Jarinu', 'Juquiá', 'Lavrinhas', 'Martinópolis', 'Serra Negra',
       'Bom Jesus dos Perdões', 'Borebi', 'Holambra', 'Itajobi',
       'Monte Azul Paulista', 'Pedro de Toledo', 'Pinhalzinho',
       'Pirapora do Bom Jesus', 'Presidente Alves',
       'Santa Cruz da Conceição', 'Santo Antônio do Aracanguá',
       'Santo Antônio do Pinhal', 'Socorro', 'Tuiuti', 'Arealva',
       'Auriflama', 'Igaraçu do Tietê', 'Ituverava', 'Pradópolis',
       'Santa Fé do Sul', 'Bocaina', 'Caconde', 'Colina', 'Cosmorama',
       'Cosmópolis', 'Guará', 'Lindóia', 'Novo Horizonte', 'Parisi',
       'Piquerobi', 'Regente Feijó', 'Ribeirão Branco',
       'Santo Antônio de Posse', 'Tupi Paulista', 'Álvares Machado',
       'Guariba', 'Paraibuna', 'Paranapanema', 'Presidente Epitácio',
       'Rio das Pedras', 'Saltinho', 'Sarapuí', 'Vargem',
       'Águas da Prata', 'Adolfo', 'Anhembi', 'Cajobi', 'Charqueada',
       'Ibitinga', 'Nova Guataporanga', 'Salto Grande',
       'Santa Maria da Serra', 'Timburi', 'Conchal', 'Coroados', 'Ibaté',
       'Itaí', 'Jacupiranga', 'Pedrinhas Paulista', 'Tarumã', 'Tietê',
       'Vargem Grande do Sul', 'Osvaldo Cruz', 'Pracinha',
       'São Pedro do Turvo', 'Iperó', 'Nova Granada', 'Bertioga',
       'Cândido Mota', 'Guaraçaí', 'Ibirarema', 'Nipoã',
       'Santa Cruz das Palmeiras', 'Sete Barras', 'Sud Mennucci', 'Uchoa',
       'Bernardino de Campos', 'Brejo Alegre', 'Cerqueira César', 'Cunha',
       'Dois Córregos', 'Dumont', 'Guapiaçu', 'Iacanga', 'Irapuru',
       'Itapura', 'Itapuí', 'Itobi', 'Jambeiro', 'Marapoama',
       'Neves Paulista', 'Patrocínio Paulista', 'Pereira Barreto',
       'Pirapozinho', 'Reginópolis', 'Santo Anastácio', 'Sarutaiá',
       'Tabatinga', 'Tapiratiba', 'Torre de Pedra', 'Torrinha', 'Uru',
       'Américo de Campos', 'Bananal', 'Canas', 'Gastão Vidigal',
       'Guareí', 'Ipuã', 'Monte Aprazível', 'Porangaba',
       'Santa Cruz da Esperança', 'São Luiz do Paraitinga', 'Tapiraí',
       'União Paulista', 'Avanhandava', 'Divinolândia',
       'Flórida Paulista', 'Getulina', 'Gália', 'Lavínia', 'Meridiano',
       'Pacaembu', 'Santo Antônio do Jardim', 'Serra Azul', 'Taguaí',
       'Taquarivaí', 'Teodoro Sampaio', 'Ubirajara', 'Viradouro',
       'Águas de Santa Bárbara', 'Álvaro de Carvalho', 'Alto Alegre',
       'Guaiçara', 'Indiana', 'Inúbia Paulista', 'Ipiguá', 'Nova Aliança',
       'Nova Campina', 'Nova Europa', 'Pedreira', 'Presidente Bernardes',
       'Valparaíso', 'Barbosa', 'Poloni', 'Catiguá', 'Silveiras',
       'Alumínio', 'Emilianópolis', 'Fernando Prestes', 'General Salgado',
       'Guapiara', 'Herculândia', 'Luís Antônio', 'Santo Expedito',
       'Tabapuã', 'Altinópolis', 'Brotas', 'Casa Branca', 'Elisiário',
       'Potirendaba', 'Ribeirão Grande', 'Ribeirão dos Índios',
       'Rubiácea', "Santa Clara d'Oeste", 'Severínia',
       'São João das Duas Pontes', 'Tambaú', 'Tremembé', 'Cerquilho',
       'Guaimbê', 'Guaraci', 'Itaberá', 'Itápolis', 'Potim', 'Roseira',
       "São João do Pau d'Alho", 'Urupês', 'Buri',
       'Campina do Monte Alegre', "Guarani d'Oeste", 'Magda', 'Mendonça',
       'Murutinga do Sul', 'Nuporanga', 'Ouroeste', 'Panorama', 'Pirangi',
       'Planalto', 'São Bento do Sapucaí', 'Altair', 'Anhumas',
       'Boracéia', 'Dourado', 'Itaoca', 'Monteiro Lobato', 'Sagres',
       'Valentim Gentil', 'Descalvado', 'Monções', 'Trabiju',
       'Cesário Lange', 'Palmares Paulista', 'Santa Adélia', 'Tejupá',
       'Alfredo Marcondes', 'Bálsamo', 'Capivari', 'Ipeúna', 'Itirapuã',
       'Manduri', 'Palestina', 'Piquete', 'Riolândia', 'Rosana', 'Sales',
       'Sales Oliveira', 'Ariranha', 'Barão de Antonina',
       'Boa Esperança do Sul', 'Pardinho', 'Pontes Gestal', 'Quadra',
       'Santópolis do Aguapeí', 'Taiúva', 'Três Fronteiras', 'Bastos',
       'Fernão', 'Macaubal', 'Onda Verde', "Palmeira d'Oeste",
       'Santa Salete', 'Zacarias', 'Cardoso', 'Cândido Rodrigues',
       'Gavião Peixoto', 'Itaporanga', 'Oriente', 'Parapuã', 'Pontalinda',
       'São Simão', 'Bofete', 'Dolcinópolis',
       'Euclides da Cunha Paulista', 'Iacri', 'Ribeirão Bonito',
       'Santa Rosa de Viterbo', 'Urânia', 'Irapuã', 'Motuca',
       'Mirante do Paranapanema', 'Pompéia', 'Novais', 'Pereiras',
       'Santana da Ponte Pensa', 'São José da Bela Vista', 'Floreal',
       'Guarantã', 'Indiaporã', 'Paulo de Faria', 'Campos Novos Paulista',
       'Coronel Macedo', 'Lutécia', 'Mariápolis', 'Paraguaçu Paulista',
       'Álvares Florence', 'Buritizal', 'Cássia dos Coqueiros', 'Paraíso',
       'Alvinlândia', 'Aspásia', 'Embaúba', 'Gabriel Monteiro',
       'Nova Luzitânia', 'Paranapuã', 'Borá', 'Echaporã', 'Taquaral',
       'Turmalina', 'Caiuá', 'Guatapará', 'João Ramalho',
       'Natividade da Serra', 'São Francisco', 'Júlio Mesquita',
       'Monte Alegre do Sul', 'Queiroz', 'Rafard', 'Redenção da Serra',
       'Ribeirão do Sul', 'Bento de Abreu', 'Corumbataí', 'Luiziânia',
       'Nova Castilho', 'Ocauçu', 'São João de Iracema', 'Braúna',
       'Marinópolis', 'Mirassolândia', 'Sebastianópolis do Sul', 'Arapeí',
       'Cabrália Paulista', 'Sabino', 'Analândia', 'Dirce Reis',
       'Ipaussu', "Aparecida d'Oeste", 'Aramina', 'Cristais Paulista',
       'Itaju', 'Paulicéia', 'Ribeira', 'Santa Ernestina', 'Ubarana',
       'Colômbia', 'Cafelândia', 'Glicério', 'Lourdes', 'Icém',
       'Espírito Santo do Turvo', 'Estrela do Norte', 'Lupércio',
       'Vera Cruz', 'Turiúba', 'Iaras', 'Balbinos', 'Barra do Chapéu',
       'Jumirim', 'Maracaí', 'Mira Estrela', 'Mombuca', 'Monte Castelo',
       'Pedranópolis', 'Rifaina', 'Óleo', 'Salmourão', 'Santa Albertina',
       'Taciba', 'Vitória Brasil', 'Queluz', 'Flora Rica',
       'Itapirapuã Paulista', 'Pedregulho', 'Platina', 'Areias',
       'Clementina', 'Narandiba', 'Riversul', 'Suzanápolis',
       'Marabá Paulista', 'Restinga', 'Mesópolis', 'Lucianópolis',
       'Oscar Bressane', 'Sandovalina', 'Iporanga', 'Orindiúva',
       'Canitar', 'Nantes', 'Ouro Verde', 'Rubinéia', 'Pongaí', 'Piacatu',
       "Santa Rita d'Oeste", 'Santa Mercedes', 'Bom Sucesso de Itararé',
       'Jeriquara', 'Nova Independência', 'Nova Canaã Paulista',
       'Lagoinha', 'Cruzália', 'São José do Barreiro', 'Florínea',
       'Arco-Íris', 'Ribeirão Corrente'], dtype=object)
```

In [15]:

```
data[data['city'] == "São Paulo"].shape[0]
```

Out[15]:

```
456
```

## 4 - Quantidade de cidades que estão com os campos nulos

In [16]:

```
data[data['city'].isnull()].shape[0]
```

Out[16]:

```
11857
```

## 5 - Gerar um relatório em CSV estado, população estimada, últimos casos confirmados e novas mortes

In [17]:

```
# Mostrando o nome das colunas
list(data.columns)
```

Out[17]:

```
['city',
 'city_ibge_code',
 'date',
 'epidemiological_week',
 'estimated_population',
 'estimated_population_2019',
 'is_last',
 'is_repeated',
 'last_available_confirmed',
 'last_available_confirmed_per_100k_inhabitants',
 'last_available_date',
 'last_available_death_rate',
 'last_available_deaths',
 'order_for_place',
 'place_type',
 'state',
 'new_confirmed',
 'new_deaths']
```

Criando um objeto "col" para inserir as colunas do Dataframe data e filtrando com 10000 registros

Atribui o objeto "col" ao objeto report.

In [18]:

```
col = data[['state', 'estimated_population', 'last_available_confirmed', 'new_deaths']].sort_values('estimated_population', ascending=False).head(10000)
report = col
```

In [19]:

```
report
```

Out[19]:

|         | state | estimated_population | last_available_confirmed | new_deaths |
| ------: | ----: | -------------------: | -----------------------: | ---------: |
| 1837165 |    SP |           46289333.0 |                    24041 |        224 |
| 2069281 |    SP |           46289333.0 |                  2956210 |        689 |
| 1887522 |    SP |           46289333.0 |                   500301 |        383 |
| 1888165 |    SP |           46289333.0 |                   514197 |        330 |
| 2004581 |    SP |           46289333.0 |                  1702294 |         54 |
|     ... |   ... |                  ... |                      ... |        ... |
|  316558 |    DF |            3055149.0 |                   164861 |         11 |
|  316056 |    DF |            3055149.0 |                      556 |          1 |
|  316054 |    DF |            3055149.0 |                      518 |          1 |
|  316053 |    DF |            3055149.0 |                      527 |          1 |
|  316051 |    DF |            3055149.0 |                      486 |          1 |

10000 rows × 4 columns

## Exportar para um arquivo CSV o dataframe

In [20]:

```
report.to_csv('./covid-19/report_covid-19.csv')
```

```git
<img src="C:\Users\Heliton\Documents\GitHub\Projeto_1_Uniasselvi\images\1.PNG" alt="img1"/>
```



## Ingestão dos dados do relatório para o Postgres

In [ ]:

```
!conda install sqlalchemy -y
```

In [ ]:

```
!conda install psycopg2 -y
```

#### Importação da biblioteca SqlAlchemy

In [21]:

```
from sqlalchemy import create_engine
```

#### Criando conexão com o postgres com o driver psycopg2

In [22]:

```
engine = create_engine(
    'postgresql+psycopg2://postgres:root@localhost/projeto1_uniasselvi'
)
```

#### Fazendo a ingestão do Dataframe para o SGBD Postgres

In [23]:

```
# Ingestão
# append, adiciona outra tabela se já existir uma tabela de mesmo nome
report.to_sql('covid_19', con=engine, index=False, if_exists='append')
```

![image-20210530130611428](C:\Users\Heliton\AppData\Roaming\Typora\typora-user-images\image-20210530130611428.png)

## Ingestão dos dados do relatório para o MySQL

In [ ]:

```
!conda install PyMySQL -y
```

#### Criando conexão com o postgres com o driver pymysql

In [24]:

```
engine = create_engine(
    'mysql+pymysql://root:root@localhost/projeto1_uniasselvi'
)
```

#### Fazendo a ingestão do Dataframe para o SGBD MySQL

In [25]:

```
# Ingestão
# append, adiciona outra tabela se já existir uma tabela de mesmo nome
report.to_sql('covid_19', con=engine, index=False, if_exists='append')
```

![image-20210530130524540](C:\Users\Heliton\AppData\Roaming\Typora\typora-user-images\image-20210530130524540.png)
