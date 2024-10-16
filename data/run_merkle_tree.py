from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from bokeh.layouts import gridplot
from parser import noir_parser_merkle, snarkjs_parser_merkle
# from bokeh.io import export_svg
import os

# runtime plot
# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/merkle_tree_results.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results_merkle_tree.json')

noir_mimc_merkle_height, noir_mimc_prove_metric, noir_griffin_merkle_height,noir_griffin_prove_metric,noir_poseidon_merkle_height, noir_poseidon_prove_metric, noir_poseidon2_merkle_height,noir_poseidon2_prove_metric = noir_parser_merkle(data_path_noir, 'prove', 'user_time')

snarkjs_mimc_merkle_height, snarkjs_mimc_prove_metric, snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, snarkjs_poseidon2_merkle_height, snarkjs_poseidon2_prove_metric, snarkjs_gmimc_merkle_height, snarkjs_gmimc_prove_metric, snarkjs_neptune_merkle_height, snarkjs_neptune_prove_metric = snarkjs_parser_merkle(data_path_snarkjs, 'prove', 'user_time')

# create a new plot with a title and axis labels
p1 = figure(title="Proof generation runtime with different Merkle tree height (MBP M1)", x_axis_label="Merkle tree height", y_axis_label="Runtime/ millisecond",width=800, height=600, y_axis_type="log", y_range=(0.01, 10.0**2))

# add multiple renderers
p1.scatter(noir_mimc_merkle_height, noir_mimc_prove_metric, legend_label="mimc/ noir-bb", size=7, marker="triangle",fill_color='navy')
p1.line(noir_mimc_merkle_height, noir_mimc_prove_metric, legend_label="mimc/ noir-bb", color="navy")

p1.scatter(noir_griffin_merkle_height, noir_griffin_prove_metric, legend_label="griffin/ noir-bb", size=7, fill_color='navy')
p1.line(noir_griffin_merkle_height, noir_griffin_prove_metric, legend_label="griffin/ noir-bb", color="navy")

p1.scatter(noir_poseidon_merkle_height, noir_poseidon_prove_metric, size=7, marker="square", legend_label="poseidon/ noir-bb", fill_color="navy")
p1.line(noir_poseidon_merkle_height, noir_poseidon_prove_metric, legend_label="poseidon/ noir-bb", color="navy")

p1.scatter(noir_poseidon2_merkle_height, noir_poseidon2_prove_metric, legend_label="poseidon2/ noir-bb", size=7, marker="plus", fill_color='navy')
p1.line(noir_poseidon2_merkle_height, noir_poseidon2_prove_metric, legend_label="poseidon2/ noir-bb", color="navy")

p1.scatter(snarkjs_mimc_merkle_height, snarkjs_mimc_prove_metric, legend_label="mimc/ circom-snarkjs", size=7, marker="triangle",fill_color='lightsteelblue')
p1.line(snarkjs_mimc_merkle_height, snarkjs_mimc_prove_metric, legend_label="mimc/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, size=7, marker="square", legend_label="poseidon/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, legend_label="poseidon/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_poseidon2_merkle_height, snarkjs_poseidon2_prove_metric, size=7, marker="plus", legend_label="poseidon2/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_poseidon2_merkle_height, snarkjs_poseidon2_prove_metric, legend_label="poseidon2/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, size=7, marker="square", legend_label="poseidon/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, legend_label="poseidon/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_gmimc_merkle_height, snarkjs_gmimc_prove_metric, size=7, marker="inverted_triangle", legend_label="gmimc/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_gmimc_merkle_height, snarkjs_gmimc_prove_metric, legend_label="gmimc/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_neptune_merkle_height, snarkjs_neptune_prove_metric, size=7, marker="square_cross", legend_label="neptune/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_neptune_merkle_height, snarkjs_neptune_prove_metric, legend_label="neptune/ circom-snarkjs", color="lightsteelblue")


p1.legend.location = "top_left"
p1.legend.title = "Hash Function/ Library"

p1.xaxis.ticker = FixedTicker(ticks=[i for i in range(0, 8)])

# p1.output_backend = "svg"

# ram plot
# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/merkle_tree_results.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results_merkle_tree.json')

noir_mimc_merkle_height, noir_mimc_prove_metric, noir_griffin_merkle_height,noir_griffin_prove_metric,noir_poseidon_merkle_height, noir_poseidon_prove_metric, noir_poseidon2_merkle_height,noir_poseidon2_prove_metric = noir_parser_merkle(data_path_noir, 'prove', 'max_resident_size')

snarkjs_mimc_merkle_height, snarkjs_mimc_prove_metric, snarkjs_poseidon_merkle_height, snarkjs_poseidon_prove_metric, snarkjs_poseidon2_merkle_height, snarkjs_poseidon2_prove_metric, snarkjs_gmimc_merkle_height, snarkjs_gmimc_prove_metric, snarkjs_neptune_merkle_height, snarkjs_neptune_prove_metric  = snarkjs_parser_merkle(data_path_snarkjs, 'prove', 'max_resident_size')

# create a new plot with a title and axis labels
p2 = figure(title="Proof generation max resident size with different Merkle tree height (MBP M1)", x_axis_label="Merkle tree height", y_axis_label="Max resident size/ kb",width=800, height=600, y_axis_type="log", y_range=(10.0**3, 10.0**7))

kb_noir_mimc_prove_metric = [int(x) / 1024 for x in noir_mimc_prove_metric]
kb_noir_griffin_prove_metric = [int(x) / 1024 for x in noir_griffin_prove_metric]
kb_noir_poseidon_prove_metric = [int(x) / 1024 for x in noir_poseidon_prove_metric]
kb_noir_poseidon2_prove_metric = [int(x) / 1024 for x in noir_poseidon2_prove_metric]
kb_snarkjs_mimc_prove_metric = [int(x) / 1024 for x in snarkjs_mimc_prove_metric]
kb_snarkjs_poseidon_prove_metric = [int(x) / 1024 for x in snarkjs_poseidon_prove_metric]
kb_snarkjs_gmimc_prove_metric = [int(x) / 1024 for x in snarkjs_gmimc_prove_metric]
kb_snarkjs_poseidon2_prove_metric = [int(x) / 1024 for x in snarkjs_poseidon2_prove_metric]
kb_snarkjs_neptune_prove_metric = [int(x) / 1024 for x in snarkjs_neptune_prove_metric]

# add multiple renderers
p2.scatter(noir_mimc_merkle_height, kb_noir_mimc_prove_metric, size=7, marker="triangle",fill_color='navy')
p2.line(noir_mimc_merkle_height, kb_noir_mimc_prove_metric, color="navy")

p2.scatter(noir_griffin_merkle_height, kb_noir_griffin_prove_metric, size=7, fill_color='navy')
p2.line(noir_griffin_merkle_height, kb_noir_griffin_prove_metric,  color="navy")

p2.scatter(noir_poseidon_merkle_height, kb_noir_poseidon_prove_metric, size=7, marker="square",  fill_color="navy")
p2.line(noir_poseidon_merkle_height, kb_noir_poseidon_prove_metric,  color="navy")

p2.scatter(noir_poseidon2_merkle_height, kb_noir_poseidon2_prove_metric, size=7, marker="plus", fill_color='navy')
p2.line(noir_poseidon2_merkle_height, kb_noir_poseidon2_prove_metric,  color="navy")

# snarkjs
p2.scatter(snarkjs_mimc_merkle_height, kb_snarkjs_mimc_prove_metric,  size=7, marker="triangle",fill_color='lightsteelblue')
p2.line(snarkjs_mimc_merkle_height, kb_snarkjs_mimc_prove_metric, color="lightsteelblue")

p2.scatter(snarkjs_poseidon_merkle_height, kb_snarkjs_poseidon_prove_metric, size=7, marker="square",  fill_color="lightsteelblue")
p2.line(snarkjs_poseidon_merkle_height, kb_snarkjs_poseidon_prove_metric, color="lightsteelblue")

p2.scatter(snarkjs_poseidon2_merkle_height, kb_snarkjs_poseidon2_prove_metric, size=7, marker="plus", fill_color='lightsteelblue')
p2.line(snarkjs_poseidon2_merkle_height, kb_snarkjs_poseidon2_prove_metric,  color="lightsteelblue")

p2.scatter(snarkjs_gmimc_merkle_height, kb_snarkjs_gmimc_prove_metric, size=7, marker="inverted_triangle",  fill_color="lightsteelblue")
p2.line(snarkjs_gmimc_merkle_height, kb_snarkjs_gmimc_prove_metric, color="lightsteelblue")

p2.scatter(snarkjs_neptune_merkle_height, kb_snarkjs_neptune_prove_metric, size=7, marker="square_cross",  fill_color="lightsteelblue")
p2.line(snarkjs_neptune_merkle_height, kb_snarkjs_neptune_prove_metric, color="lightsteelblue")



# p2.legend.location = "bottom_right"
# p2.legend.title = "Hash Function/ Library"

p2.xaxis.ticker = FixedTicker(ticks=[i for i in range(0, 8)])

# p2.output_backend = "svg"

# show the results
show(gridplot([p1, p2], ncols=2, width=600, height=600))