# me - this DAT.
# 
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.


def onTableChange(dat):
	return

def onRowChange(dat, rows):
	return

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	
	# get the column with probabilites from the table
	probs = dat.col(1)

	# remove the column name from the list
	probs.pop(0)

	# sum the probability values
	op('sum_probs').par.value0 = sum(probs)

	return

def onSizeChange(dat):
	return

	