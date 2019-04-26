# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return


# When a new random number between 0 and the sum of all the probability weights is chosen,
# choose a state based on on it's assigned probability.
# @author	Michael Dean <contact@michaeldean.ca>
# @see 		https://medium.com/@peterkellyonline/weighted-random-selection-3ff222917eb6
#
# @param	val		Some random number between 0 and the sum of all possible probabilities
# @return	A new state, based on it's assigned probability.
def onValueChange(channel, sampleIndex, val, prev):

	# Pick a number at random between 1 and the sum of the weights
	randomWeight = val;

	# Get the list of probabilities from a table containing all probabilities in a column
	probWeights = op('probabilities').col(1)

	# Drop the title from the list
	probWeights.pop(0)

	# iterate over the items
	for i, weight in enumerate(probWeights):

		# For the current item, subtract the itemâ€™s weight 
		# from the random number that was originally picked
		randomWeight = randomWeight - weight

		# Compare to zero. The larger the weight, the less likely
		# to be less than zero when compared to random selection
		# between zero and sum of the weights. 
		if randomWeight <= 0:
			op('state').par.value0 = i+1
			break

		# If not less than zero, keep subtracting weights by iterating
		# through the list.
	return
	