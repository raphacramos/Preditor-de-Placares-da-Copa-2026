import re
import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Título do cabeçalho
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Relatorio de Metodologia Preditiva - Copa do Mundo FIFA 2026', align='L')
        # self.ln(0) é desnecessário se mudarmos para novas coordenadas
        self.set_x(10) # Volta para a esquerda ou usa o posicionamento padrão
        self.cell(0, 10, 'Google DeepMind Antigravity', align='R')
        self.ln(10)
        self.line(10, 18, 200, 18)
        self.ln(2)

    def footer(self):
        # Rodapé com número de página
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.line(10, self.get_y() - 2, 200, self.get_y() - 2)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', align='C')

def limpar_texto(text):
    # Remove qualquer caracter fora do Latin-1 (como emojis, bandeiras, símbolos matemáticos gregos não-latinos)
    latin1_pattern = re.compile(r'[^\x00-\xff]')
    
    # Substituições de fórmulas LaTeX para formato textual claro e legível
    replacements = {
        r"$$\lambda_A = \alpha_A \cdot \beta_B \cdot \text{factor}_A$$": "lambda_A = alpha_A * beta_B * factor_A",
        r"$$\lambda_B = \alpha_B \cdot \beta_A \cdot \text{factor}_B$$": "lambda_B = alpha_B * beta_A * factor_B",
        r"$\lambda_a, \lambda_b$": "lambda_a, lambda_b",
        r"$\lambda_A$": "lambda_A",
        r"$\lambda_B$": "lambda_B",
        r"$\alpha$": "alpha",
        r"$\beta$": "beta",
        r"$\gamma$": "gamma",
        r"$\rho$": "rho",
        r"$\text{factor}$": "factor",
        r"$\hat{d}$": "d_esperado",
        r"$$d' = \text{sinal}(d) \cdot 3 \log_{10}(1 + |d|)$$": "d_transf = sinal(d) * 3 * log10(1 + |d|)",
        r"$d$": "d",
        r"$d'$": "d_transf",
        r"$d = G_H - G_A$": "d = G_H - G_A",
        r"$R_H$": "Rating_Casa",
        r"$R_A$": "Rating_Fora",
        r"$R_{H}$": "Rating_Casa",
        r"$R_{A}$": "Rating_Fora",
        r"$R_{H, A}$": "Rating_Casa(A)",
        r"$R_{A, B}$": "Rating_Fora(B)",
        r"$\lambda_{\text{learn}} = 0.07$": "lambda_aprendizado = 0.07",
        r"$\lambda_{\text{reg}} = \mathbf{5.0}$": "lambda_reg = 5.0",
        r"$\lambda_{\text{shrink}} = \mathbf{0.1}$": "lambda_shrink = 0.1",
        r"$\delta$": "delta",
        r"$\lambda_A^* = \lambda_A \cdot \frac{\delta_A}{\delta_B} \quad \text{e} \quad \lambda_B^* = \lambda_B \cdot \frac{\delta_B}{\delta_A}$": "lambda_A_final = lambda_A * (delta_A / delta_b) e lambda_B_final = lambda_B * (delta_B / delta_A)",
        r"$\lambda_a^* = \lambda_a \cdot (\delta_a / \delta_b)$": "lambda_a_final = lambda_a * (delta_a / delta_b)",
        r"$\lambda_b^* = \lambda_b \cdot (\delta_b / \delta_a)$": "lambda_b_final = lambda_b * (delta_b / delta_a)",
        r"$\gamma_{\text{casa}}$": "gamma_casa",
        r"$\gamma_{\text{fora}}$": "gamma_fora",
        r"$\theta$": "theta",
        r"$\tau$": "tau",
        r"$\tau(x, y)$": "tau(x, y)",
        r"$$\text{Fadiga} = \frac{\text{Distância (km)}}{1000} - \text{Dias de Descanso} + \frac{\text{Temperatura} - 20}{10}$$": "Fadiga = (Distancia / 1000) - Dias_Descanso + (Temp - 20) / 10",
        r"$$\delta = \exp(-\theta \cdot \text{Fadiga})$$": "delta = exp(-theta * Fadiga)",
        r"$$\text{Loss} = \text{NLL} + \lambda_{\text{reg}} \sum_j [(\alpha_j - \alpha_{\text{prior}, j})^2 + (\beta_j - \beta_{\text{prior}, j})^2] + \lambda_{\text{shrink}} \sum_j [(\alpha_j - 1.0)^2 + (\beta_j - 1.0)^2]$$": "Loss = NLL + lambda_reg * sum((alpha_j - alpha_prior)^2 + (beta_j - beta_prior)^2) + lambda_shrink * sum((alpha_j - 1.0)^2 + (beta_j - 1.0)^2)",
        r"$\alpha_j, \beta_j$": "alpha_j, beta_j",
        r"$\alpha_{\text{prior}, j}, \beta_{\text{prior}, j}$": "alpha_prior, beta_prior",
        r"$\lambda_{\text{reg}}$": "lambda_reg",
        r"$\lambda_{\text{shrink}}$": "lambda_shrink",
        r"$\sum R = 0$": "soma(R) == 0",
        r"$\gamma = 1.25$": "gamma = 1.25",
        r"$\rho = -0.1500$": "rho = -0.1500",
        r"$\delta_A$": "delta_A",
        r"$\delta_B$": "delta_B",
        r"$\delta_a$": "delta_a",
        r"$\delta_b$": "delta_b",
        r"$\lambda$": "lambda",
        r"$\Delta \text{lat}$": "delta_lat",
        r"$\Delta \text{lon}$": "delta_lon",
        r"$\text{lat}_1$": "lat_1",
        r"$\text{lat}_2$": "lat_2",
        r"$$d = 2R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \text{lat}}{2}\right) + \cos(\text{lat}_1)\cos(\text{lat}_2)\sin^2\left(\frac{\Delta \text{lon}}{2}\right)}\right)$$": "d = 2 * R * arcsin( sqrt( sin^2(delta_lat/2) + cos(lat1)*cos(lat2)*sin^2(delta_lon/2) ) )",
        r"$$\text{boost} = 1.0 + 0.18 \cdot (R - 1.8)$$": "boost = 1.0 + 0.18 * (R - 1.8)",
        r"$$\lambda_{\text{fav}}^* = \lambda_{\text{fav}} \cdot \text{boost}$$": "lambda_fav_final = lambda_fav * boost",
        r"$$\lambda_{\text{und}}^* = \lambda_{\text{und}} \cdot 0.90$$": "lambda_und_final = lambda_und * 0.90",
        r"$\lambda_{\text{fav}}^* = \lambda_{\text{fav}} \cdot \text{boost}$": "lambda_fav_final = lambda_fav * boost",
        r"$\lambda_{\text{und}}^* = \lambda_{\text{und}} \cdot 0.90$": "lambda_und_final = lambda_und * 0.90"
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
        
    # Limpa tags markdown de bold/italic
    text = text.replace("**", "").replace("*", "")
    
    # Executa a limpeza Latin-1 final
    text = latin1_pattern.sub(r"", text)
    
    return text.strip()

def converter_markdown_para_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove o bloco de arquitetura do mermaid
    content = re.sub(r"```mermaid.*?```", "[Diagrama de Arquitetura - Disponivel no Relatorio Markdown]", content, flags=re.DOTALL)

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    lines = content.split("\n")
    in_table = False
    table_headers = []
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Ignora linhas divisórias de tabela
        if in_table and re.match(r"^\|?\s*:?-+:?\s*\|", line):
            i += 1
            continue
            
        # Processa tabelas
        if line.startswith("|"):
            in_table = True
            parts = [limpar_texto(p) for p in line.split("|")[1:-1]]
            if not table_headers:
                table_headers = parts
            else:
                table_rows.append(parts)
            i += 1
            continue
        elif in_table:
            # Renderiza a tabela concluída
            in_table = False
            pdf.ln(2)
            with pdf.table(col_widths=None) as table:
                # Cabeçalho
                row = table.row()
                pdf.set_font('Helvetica', 'B', 8.5)
                for h in table_headers:
                    row.cell(h)
                # Dados
                pdf.set_font('Helvetica', '', 8)
                for r in table_rows:
                    row = table.row()
                    for c in r:
                        row.cell(c)
            pdf.ln(5)
            table_headers = []
            table_rows = []
            
        if line == "":
            i += 1
            continue
            
        # Título principal
        if line.startswith("# "):
            title = limpar_texto(line[2:])
            pdf.set_font('Helvetica', 'B', 15)
            pdf.set_text_color(26, 54, 93)
            pdf.multi_cell(0, 8, title)
            pdf.ln(4)
            
        # Título secundário
        elif line.startswith("## "):
            title = limpar_texto(line[3:])
            pdf.set_font('Helvetica', 'B', 11.5)
            pdf.set_text_color(44, 82, 130)
            pdf.ln(2)
            pdf.multi_cell(0, 7, title)
            pdf.ln(2)
            
        # Título terciário
        elif line.startswith("### "):
            title = limpar_texto(line[4:])
            pdf.set_font('Helvetica', 'B', 10)
            pdf.set_text_color(74, 85, 104)
            pdf.multi_cell(0, 5, title)
            pdf.ln(2)
            
        # Listas ordenadas e não ordenadas
        elif line.startswith("* ") or line.startswith("- ") or line.startswith("1. ") or line.startswith("2. ") or line.startswith("3. ") or line.startswith("4. ") or line.startswith("5. "):
            bullet_char = "- " if line.startswith("* ") or line.startswith("- ") else ""
            clean_line = line[2:] if line.startswith("* ") or line.startswith("- ") else line
            clean_text = limpar_texto(clean_line)
            pdf.set_font('Helvetica', '', 9)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 5, f"  {bullet_char}{clean_text}")
            pdf.ln(1)
            
        # Box de citações ou destaques
        elif line.startswith(">"):
            pdf.set_font('Helvetica', 'I', 9)
            pdf.set_text_color(128, 0, 0)
            clean_text = limpar_texto(line.replace(">", "").replace("[!IMPORTANT]", "").replace("[!NOTE]", "").replace("[!TIP]", ""))
            pdf.multi_cell(0, 5, f"  [Destaque] {clean_text}")
            pdf.ln(2)
            
        # Parágrafos normais
        else:
            pdf.set_font('Helvetica', '', 9.5)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 5.5, limpar_texto(line))
            pdf.ln(2.5)
            
        i += 1

    pdf.output(pdf_path)
    print(f"PDF gerado com sucesso em: {pdf_path}")

if __name__ == "__main__":
    md = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/relatorio_metodologia_preditiva.md"
    pdf = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/relatorio_metodologia_preditiva.pdf"
    converter_markdown_para_pdf(md, pdf)
