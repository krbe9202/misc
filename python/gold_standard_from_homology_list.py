import os, csv
from collections import defaultdict

# Path to files
homology_tsv="FILENAME" 
pos_goldStandard_tsv="FILENAME" 
neg_goldStandard_tsv="FILENAME"

############################ 

def make_dict(file):
	"""
	Parse file and create dictionary
	"""
	dictionary = defaultdict(list) 
	with open(file) as f:
		for line in f: 
			(key,value) = line.strip().split('\t')
			dictionary[key].append(value)
	return dictionary

def switch_genes(gS_dict, homology_dict):
	"""
	Substitute gS genes for the homologous genes 
	"""

	print("Set of genes that are in goldStandard but not in homology list: \n%s" % list(set(gS_dict.keys()) - set(homology_dict.keys())))
	for (gS_dict_key,gS_dict_val) in list(gS_dict.items()):
		if gS_dict_key in homology_dict.keys():
			hkey = str(homology_dict.get(gS_dict_key))
			gS_dict[hkey] = gS_dict.pop(gS_dict_key)
			gS_dict[hkey] = []
			for hval in [homology_dict[v] for v in gS_dict_val]:
				if len(hval) >= 1: 
					gS_dict[hkey].append(hval)
		else: 
			gS_dict.pop(gS_dict_key)

	return gS_dict

def write_tsv(filename,hm_dict, verbose=False):
	"""
	Write TSV file 
	"""
	with open(filename, 'w') as f: 
		for key, value in hm_dict.items():
			for val in value: 
				f.write('%s\t%s\n' % (key.strip("'[]'"), ''.join(val).strip()))


############################

pos_gS_dict = make_dict(pos_goldStandard_tsv)
neg_gS_dict = make_dict(neg_goldStandard_tsv)
homology_dict = make_dict(homology_tsv)

hm_pos_gS_dict = switch_genes(pos_gS_dict, homology_dict)
hm_neg_gS_dict = switch_genes(neg_gS_dict, homology_dict)

write_tsv("FILENAME",hm_pos_gS_dict)
write_tsv("FILENAME",hm_neg_gS_dict)



