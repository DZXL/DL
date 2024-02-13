import numpy as np
import assignment

def test_get_single_layer_model_props():
	# Check that you're actually making a model
	model_args = assignment.get_single_layer_model_components()

	assert model_args.model != None
	assert type(model_args.model) is assignment.SingleLayerModel
	assert model_args.epochs != None
	assert type(model_args.epochs) is int
	print("Simplest model props test passed!")

def test_get_single_layer_model_return():
	# Check model output shape
	model_args = assignment.get_single_layer_model_components()

	fake_data = np.zeros((353, 10))

	assert model_args.model(fake_data).shape == (353, 1)
	print("Simplest model return shape test passed!")


if __name__ == '__main__':
	'''
	Uncomment the tests you would like to run for sanity checks throughout the assignment
	'''
	
	### Simplest model props test ###
	test_get_single_layer_model_props()

	### Simplest model return shape test ###
	test_get_single_layer_model_return()
	
