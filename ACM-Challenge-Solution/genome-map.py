# Keerthi Srilakshmidaran
# Circular Genome Map of Tomato Curly Stunt Virus NC_004675

# BioPython and GenomeDiagram were used to read the GenBank file with
# SeqRecord and customize features of the diagram.

import Bio
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm
from PIL import Image

# read in GenBank file as a SeqIO object
with open('/Users/keerthisri/desktop/data/Genome.gb', 'r', encoding="utf-8") as genome:
    gb_file = SeqIO.read(genome, "genbank")

# create an empty diagram with an empty track and feature set
gd_map = GenomeDiagram.Diagram("Tomato curly stunt virus")
gd_track = gd_map.new_track(1, name="Annotated Features")
gd_features = gd_track.new_set('feature')

# loop through all features to add to feature set
for feature in gb_file.features:
    # checks if feature is a gene
    if feature.type == "CDS":
        # alternate colors
        if len(gd_features) % 2 == 0:
            color = colors.saddlebrown
        else:
            color = colors.burlywood

        # add features and labels to feature set
        gd_features.add_feature(feature, label=True, label_size=25,
                                color=color)

# make, save, and display output file
gd_map.draw(format="circular", circular=True, pagesize=(50 * cm, 50 * cm),
            start=0, end=len(gb_file), circle_core=0.7)
gd_map.write("/Users/keerthisri/desktop/data/circular-genome.jpg", "JPG")

map_img = Image.open("/Users/keerthisri/desktop/data/circular-genome.jpg")
map_img.show()
