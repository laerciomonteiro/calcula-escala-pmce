# Calcula Escala PMCE ⚖️📅

Ferramenta em Python para cálculo automático da escala de serviço do Patrulhamento Ostensivo Geral (POG) da Polícia Militar do Ceará, seguindo os modelos 12h/24h e 12h/48h.

## Funcionalidades Principais
- Cálculo automático dos turnos A e B
- Suporte aos dois modelos de escala:
  - **12h/24h** (Plantão de 12 horas com 24 de descanso)
  - **12h/48h** (Plantão de 12 horas com 48 de descanso)
- Geração de tabela cronológica com datas futuras de serviço
- Interface intuitiva via linha de comando

## Pré-requisitos
- Python 3.6 ou superior instalado
- Sistema operacional compatível com Python (Windows/Linux/macOS)

## Instalação e Uso
1. Clone o repositório:
```bash
git clone https://github.com/laerciomonteiro/calcula-escala-pmce.git
```
2. Acesse o diretório:
```bash
cd calcula-escala-pmce
```
3. Execute o script:
```bash
python3 calcula-escala.py
```

## Fluxo de Operação
1. O sistema solicitará:
- Data do turno A (DD/MM/AAAA)
- Data do turno B (DD/MM/AAAA)
- Quantidade de turnos futuros a serem exibidos

2. Saída gerada:
```bash
+------------+-----------+-----------------------+
| Data | Turno | Modelo de Escala |
+------------+-----------+-----------------------+
| 15/03/2025 | A | 12h/24h |
| 16/03/2025 | Descanso | |
| 17/03/2025 | B | 12h/24h |
+------------+-----------+-----------------------+
```

## Personalização
- Ajuste o número de turnos futuros conforme necessidade operacional

## Licença
`MIT License` - Consulte o arquivo LICENSE para detalhes.

## Autor
**Laércio Monteiro**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/laercio-monteiro)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram)](https://instagram.com/laercio.monteiro_)

✉️ Contato profissional: laercio@betacoding.com.br

---

⚙️ *Ferramenta desenvolvida por profissional de segurança pública com expertise em desenvolvimento de soluções tecnológicas para operacionalidade policial*
