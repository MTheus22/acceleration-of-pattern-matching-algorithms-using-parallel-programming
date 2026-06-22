import matplotlib.pyplot as plt
import numpy as np

# Configurar estilo do gráfico
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)

# Dados do results.tex
threads = np.array([1, 4, 8, 12])
speedup_snort = np.array([1.04, 2.43, 3.61, 4.52])
speedup_et = np.array([1.14, 1.98, 2.64, 2.79])

# Linha ideal
ideal_threads = np.arange(1, 13)
ideal_speedup = ideal_threads

# Plotar
ax.plot(ideal_threads, ideal_speedup, linestyle='--', color='#9ca3af', linewidth=1.5, label='Ideal (Linear)')
ax.plot(threads, speedup_snort, marker='s', markersize=8, color='#2563eb', linewidth=2.5, label='Snort (55 MiB - Cache Resident)')
ax.plot(threads, speedup_et, marker='^', markersize=9, color='#ef4444', linewidth=2.5, label='Emerging Threats (507 MiB - Memory-bound)')

# Customização dos eixos
ax.set_xlim(1, 12)
ax.set_ylim(1, 6)
ax.set_xticks([1, 2, 4, 6, 8, 10, 12])
ax.set_yticks([1, 2, 3, 4, 5, 6])

# Rótulos e legendas (em português)
ax.set_xlabel('Número de Threads ($T$)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Speedup vs. Sequencial', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('Escalabilidade do Paralelismo de Texto por Dicionário', fontsize=13, fontweight='bold', pad=15)

# Legenda estilizada
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#e2e8f0', fontsize=10)

# Grid mais suave
ax.grid(True, linestyle=':', alpha=0.6, color='#cbd5e1')

# Remover bordas desnecessárias
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Adicionar destaques visuais (anotações de regressão)
ax.annotate('Saturação da banda\nde memória (DRAM)', xy=(12, 2.79), xytext=(8.5, 1.8),
            arrowprops=dict(facecolor='#ef4444', shrink=0.08, width=1.5, headwidth=6),
            fontsize=9.5, color='#b91c1c', fontweight='bold', ha='center')

ax.annotate('Pico: 4,52x', xy=(12, 4.52), xytext=(10.5, 4.8),
            arrowprops=dict(facecolor='#2563eb', shrink=0.08, width=1.5, headwidth=6),
            fontsize=9.5, color='#1d4ed8', fontweight='bold', ha='center')

plt.tight_layout()

# Salvar imagem
output_path = '/home/matheusbarros/projects/idp/tcc/acceleration-of-pattern-matching-algorithms-using-parallel-programming/figuras/speedup_results.png'
plt.savefig(output_path, bbox_inches='tight')
print(f"Gráfico gerado com sucesso em: {output_path}")
