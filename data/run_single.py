from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from bokeh.layouts import gridplot
import os

# runtime plot

# noir
noir_hash = ['mimc', 'griffin', 'poseidon', 'poseidon2']
noir_runtime = [0.512, 0.555, 0.557, 0.530]
noir_ram = [172764365, 180631962,219629158,180402586]

# snarkjs
snarkjs_hash = ['mimc', 'gmimc', 'poseidon', 'poseidon2', 'neptune']
snarkjs_runtime = [0.49, 0.59, 0.44, 0.43,0.47]
snarkjs_ram = [219758592,202266560,192020480,174446976,175544640 ]

# plonky2
plonky2_hash = ['poseidon', 'poseidon2', 'monolith', 'griffin', 'arion', 'anemoi', 'mimc','rescue_prime']
plonky2_runtime = [0.016, 0.005, 0.007, 0.040,0.056,0.025,0.023,0.031]
plonky2_ram = [3522560,3571712,3571712,18857984,32358400,18939904,7503872,3670016 ]

# halo2
halo2_fp_hash = ['poseidon']
halo2_fp_runtime = [0.060]
halo2_fp_ram = [4341760]

halo2_pallas_hash = ['mimc']
halo2_pallas_runtime = [0.055]
halo2_pallas_ram = [3981312]

halo2_vesta_hash = ['mimc']
halo2_vesta_runtime = [ 0.045]
halo2_vesta_ram = [3997696]

# boojum
boojum_hash = ['poseidon2']
boojum_runtime = [0.037]
boojum_ram = [7389184]

# create a new plot with a title and axis labels
p1 = figure(title="Proof generation runtime (MBP M1)", x_axis_label="Hash functions", y_axis_label="Runtime/ millisecond",width=800, height=600, y_axis_type="log", y_range=(0.001, 10.0))

# add multiple renderers
p1.scatter(noir_hash, noir_runtime, legend_label="bn254, noir-bb", size=7, marker="circle",fill_color='navy')

p1.scatter(snarkjs_hash, snarkjs_runtime, legend_label="bn254, circom-snarkjs", size=7,marker="square", fill_color='navy')

p1.scatter(plonky2_hash, plonky2_runtime, size=7, marker="plus", legend_label="goldilocks, plonky2", fill_color="navy")

p1.scatter(halo2_fp_hash, halo2_fp_runtime, legend_label="pasta, halo2-kzg", size=7, marker="triangle", fill_color='navy')

p1.scatter(halo2_fp_hash, halo2_fp_runtime, legend_label="vesta, halo2-kzg", size=7, marker="triangle_pin", fill_color='navy')

p1.scatter(halo2_fp_hash, halo2_fp_runtime, legend_label="pallas, halo2-kzg", size=7, marker="triangle_dot", fill_color='navy')

p1.scatter(boojum_hash, boojum_runtime, legend_label="goldilocks, boojum", size=7, marker="diamond", fill_color='navy')

p1.legend.location = "top_left"
p1.legend.title = "Curve/ Framework"

# p1.xaxis.ticker = FixedTicker(ticks=['poseidon', 'poseidon2', 'monolith', 'griffin', 'arion', 'anemoi', 'mimc','rescue_prime','gmimc','neptune'])

# p1.output_backend = "svg"

# create a new plot with a title and axis labels
p2 = figure(title="Proof generation max resident size (MBP M1)", x_axis_label="Merkle tree height", y_axis_label="Max resident size/ kb",width=800, height=600, y_axis_type="log", y_range=(10.0**3, 10.0**6))

kb_noir_ram = [x / 1024 for x in noir_ram]
kb_plonky2_ram = [x / 1024 for x in plonky2_ram]
kb_halo2_fp_ram = [x / 1024 for x in halo2_fp_ram]
kb_halo2_pallas_ram = [x / 1024 for x in halo2_pallas_ram]
kb_halo2_vesta_ram = [x / 1024 for x in halo2_vesta_ram]
kb_snarkjs_ram = [x / 1024 for x in snarkjs_ram]
kb_boojum_ram = [x / 1024 for x in boojum_ram]

# add multiple renderers
p2.scatter(noir_hash, kb_noir_ram, legend_label="bn254, noir-bb", size=7, marker="circle",fill_color='navy')

p2.scatter(snarkjs_hash, kb_snarkjs_ram, legend_label="bn254, circom-snarkjs", size=7,marker="square", fill_color='navy')

p2.scatter(plonky2_hash, kb_plonky2_ram, legend_label="goldilocks, plonky2", size=7, marker="plus", fill_color="navy")

p2.scatter(halo2_fp_hash, kb_halo2_fp_ram, legend_label="pasta, halo2-kzg", size=7, marker="triangle", fill_color='navy')

p2.scatter(halo2_vesta_hash, kb_halo2_vesta_ram, legend_label="vesta, halo2-kzg", size=7, marker="triangle_pin", fill_color='navy')

p2.scatter(halo2_pallas_hash, kb_halo2_pallas_ram, legend_label="pallas, halo2-kzg", size=7, marker="triangle_dot", fill_color='navy')

p2.scatter(boojum_hash, kb_boojum_ram, legend_label="goldilocks, boojum", size=7, marker="diamond", fill_color='navy')

# p2.legend.location = "bottom_right"
# p2.legend.title = "Hash Function/ Library"

# p2.xaxis.ticker = FixedTicker(ticks=['poseidon', 'poseidon2', 'monolith', 'griffin', 'arion', 'anemoi', 'mimc','rescue_prime','gmimc','neptune'])

# p2.output_backend = "svg"

# show the results
show(gridplot([p1, p2], ncols=2, width=600, height=600))