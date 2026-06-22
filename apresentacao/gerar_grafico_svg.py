import os

# Dados
threads = [1, 4, 8, 12]
snort_speedup = [1.04, 2.43, 3.61, 4.52]
et_speedup = [1.14, 1.98, 2.64, 2.79]

# Configurações do SVG
width = 800
height = 550
margin_left = 90
margin_right = 50
margin_top = 80
margin_bottom = 70

plot_width = width - margin_left - margin_right
plot_height = height - margin_top - margin_bottom

# Limites dos eixos
x_min, x_max = 1, 12
y_min, y_max = 0, 6

def get_x(t):
    return margin_left + (t - x_min) / (x_max - x_min) * plot_width

def get_y(s):
    return margin_top + plot_height - (s - y_min) / (y_max - y_min) * plot_height

# Começar string do SVG
svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')

# Estilos CSS internos
svg.append("""
<style>
    .bg { fill: #ffffff; }
    .grid-line { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 2 2; }
    .axis { stroke: #64748b; stroke-width: 1.5; }
    .axis-label { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; fill: #334155; font-weight: bold; }
    .tick-label { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; fill: #64748b; }
    .title { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 18px; fill: #1e293b; font-weight: bold; text-anchor: middle; }
    .legend-text { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; fill: #334155; }
    .ideal-line { stroke: #94a3b8; stroke-width: 2; stroke-dasharray: 6 4; }
    .snort-line { stroke: #2563eb; stroke-width: 3; fill: none; stroke-linecap: round; stroke-linejoin: round; }
    .et-line { stroke: #ef4444; stroke-width: 3; fill: none; stroke-linecap: round; stroke-linejoin: round; }
    .snort-marker { fill: #2563eb; stroke: #ffffff; stroke-width: 1.5; }
    .et-marker { fill: #ef4444; stroke: #ffffff; stroke-width: 1.5; }
    .annotation-text { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 11px; font-weight: bold; }
    .annotation-arrow { stroke-width: 1.5; fill: none; }
</style>
""")

# Retângulo de fundo
svg.append(f'<rect width="{width}" height="{height}" class="bg"/>')

# Grid horizontal
for y_val in range(y_min, y_max + 1):
    y_pos = get_y(y_val)
    svg.append(f'<line x1="{margin_left}" y1="{y_pos}" x2="{width - margin_right}" y2="{y_pos}" class="grid-line"/>')
    # Ticks e labels do eixo Y
    svg.append(f'<text x="{margin_left - 15}" y="{y_pos + 4}" text-anchor="end" class="tick-label">{y_val},0x</text>')

# Grid vertical para threads chave (1, 2, 4, 6, 8, 10, 12)
x_ticks = [1, 2, 4, 6, 8, 10, 12]
for x_val in x_ticks:
    x_pos = get_x(x_val)
    svg.append(f'<line x1="{x_pos}" y1="{margin_top}" x2="{x_pos}" y2="{height - margin_bottom}" class="grid-line"/>')
    # Labels do eixo X
    svg.append(f'<text x="{x_pos}" y="{height - margin_bottom + 20}" text-anchor="middle" class="tick-label">{x_val}</text>')

# Linhas de eixos
svg.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height - margin_bottom}" class="axis"/>') # Y axis
svg.append(f'<line x1="{margin_left}" y1="{height - margin_bottom}" x2="{width - margin_right}" y2="{height - margin_bottom}" class="axis"/>') # X axis

# Rótulos dos eixos
svg.append(f'<text x="{margin_left + plot_width/2}" y="{height - margin_bottom + 45}" text-anchor="middle" class="axis-label">Número de Threads (T)</text>')
svg.append(f'<text x="25" y="{margin_top + plot_height/2}" text-anchor="middle" transform="rotate(-90 25 {margin_top + plot_height/2})" class="axis-label">Speedup vs. Sequencial</text>')
svg.append(f'<text x="{width/2}" y="40" class="title">Escalabilidade do Paralelismo de Texto por Dicionário</text>')

# Desenhar Linha Ideal (Linear)
x1_id, y1_id = get_x(1), get_y(1)
x2_id, y2_id = get_x(6), get_y(6) # ideal speedup = threads, so up to 6x speedup at 6 threads
svg.append(f'<line x1="{x1_id}" y1="{y1_id}" x2="{x2_id}" y2="{y2_id}" class="ideal-line"/>')

# Desenhar Linha Snort
snort_pts = []
for t, s in zip(threads, snort_speedup):
    snort_pts.append(f"{get_x(t)},{get_y(s)}")
svg.append(f'<polyline points="{" ".join(snort_pts)}" class="snort-line"/>')

# Desenhar Linha Emerging Threats
et_pts = []
for t, s in zip(threads, et_speedup):
    et_pts.append(f"{get_x(t)},{get_y(s)}")
svg.append(f'<polyline points="{" ".join(et_pts)}" class="et-line"/>')

# Marcadores Snort (Quadrados)
for t, s in zip(threads, snort_speedup):
    cx, cy = get_x(t), get_y(s)
    svg.append(f'<rect x="{cx - 5}" y="{cy - 5}" width="10" height="10" class="snort-marker"/>')

# Marcadores Emerging Threats (Triângulos)
for t, s in zip(threads, et_speedup):
    cx, cy = get_x(t), get_y(s)
    # Triângulo centrado em (cx, cy)
    pts = f"{cx},{cy - 6} {cx - 6},{cy + 5} {cx + 6},{cy + 5}"
    svg.append(f'<polygon points="{pts}" class="et-marker"/>')

# Adicionar Destaques Visuais (Anotações)
# Anotação Snort (Pico 4.52x)
snort_pico_x, snort_pico_y = get_x(12), get_y(4.52)
svg.append(f'<path d="M {snort_pico_x - 30} {snort_pico_y - 20} L {snort_pico_x - 8} {snort_pico_y - 5}" class="annotation-arrow" stroke="#2563eb" marker-end="url(#arrow-blue)"/>')
svg.append(f'<text x="{snort_pico_x - 35}" y="{snort_pico_y - 25}" text-anchor="end" class="annotation-text" fill="#1d4ed8">Pico: 4,52x (12 threads)</text>')

# Anotação Emerging Threats (Saturação)
et_pico_x, et_pico_y = get_x(12), get_y(2.79)
svg.append(f'<path d="M {et_pico_x - 40} {et_pico_y + 40} L {et_pico_x - 10} {et_pico_y + 10}" class="annotation-arrow" stroke="#ef4444" marker-end="url(#arrow-red)"/>')
svg.append(f'<text x="{et_pico_x - 45}" y="{et_pico_y + 45}" text-anchor="end" class="annotation-text" fill="#b91c1c">Saturação da banda de memória (DRAM)</text>')
svg.append(f'<text x="{et_pico_x - 45}" y="{et_pico_y + 58}" text-anchor="end" class="annotation-text" fill="#b91c1c" style="font-size:10px; font-weight:normal;">Queda de eficiência com E-cores adicionais</text>')

# Legenda
leg_x = margin_left + 20
leg_y = margin_top + 20
svg.append(f'<rect x="{leg_x}" y="{leg_y}" width="340" height="90" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" rx="4"/>')

# Item 1: Ideal
svg.append(f'<line x1="{leg_x + 15}" y1="{leg_y + 20}" x2="{leg_x + 45}" y2="{leg_y + 20}" class="ideal-line"/>')
svg.append(f'<text x="{leg_x + 55}" y="{leg_y + 24}" class="legend-text">Ideal (Linear)</text>')

# Item 2: Snort
svg.append(f'<line x1="{leg_x + 15}" y1="{leg_y + 45}" x2="{leg_x + 45}" y2="{leg_y + 45}" class="snort-line"/>')
svg.append(f'<rect x="{leg_x + 25}" y="{leg_y + 40}" width="10" height="10" class="snort-marker"/>')
svg.append(f'<text x="{leg_x + 55}" y="{leg_y + 49}" class="legend-text">Snort (55 MiB - Excede a L3, regime moderado)</text>')

# Item 3: Emerging Threats
svg.append(f'<line x1="{leg_x + 15}" y1="{leg_y + 70}" x2="{leg_x + 45}" y2="{leg_y + 70}" class="et-line"/>')
svg.append(f'<polygon points="{leg_x + 30},{leg_y + 64} {leg_x + 24},{leg_y + 75} {leg_x + 36},{leg_y + 75}" class="et-marker"/>')
svg.append(f'<text x="{leg_x + 55}" y="{leg_y + 74}" class="legend-text">Emerging Threats (507 MiB - Limitado por DRAM)</text>')

# Definições para marcadores de seta
svg.append("""
<defs>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444" />
    </marker>
</defs>
""")

svg.append('</svg>')

# Salvar arquivo
output_path = '/home/matheusbarros/projects/idp/tcc/acceleration-of-pattern-matching-algorithms-using-parallel-programming/apresentacao/figuras/speedup_results.svg'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print(f"Gráfico SVG gerado com sucesso em: {output_path}")
