# import pickle
# import h5py


# with open("assistant_model_words.pkl", "rb") as f:
#     data = pickle.load(f)

# print(data)


# with h5py.File('assistant_model.h5', 'r') as f:
#     # List the keys in the file
#     print(list(f.values()))
    
    # Read data from a dataset
#     dataset = f['assistant_model']
#     datas = dataset[:]

# print(datas)
###############################################################################################################
# import pickle

# # Load the PKL file
# with open('assistant_model_classes.pkl', 'rb') as f:
#     data = pickle.load(f)

# # Open a text file in write mode
# with open('assistant_model_classes.txt', 'w') as f:
#     # Write the data to the text file
#     f.write(str(data))

# # Close the text file
# f.close()
###################################################################################################################

import h5py

# Load the H5 file
# with h5py.File('assistant_model.h5', 'r') as f:
#     data = f['model_weights'][:]

# # Open a text file in write mode
# with open('assistant_model.txt', 'w') as f:
#     # Write the data to the text file
#     for d in data:
#         f.write(str(d) + '\n')

# with h5py.File('assistant_model.h5', 'r') as f:
#     # Print the keys of all groups and datasets in the file
#     for key in f.keys():
#         print(key)

# # Close the text file
# f.close()

with h5py.File('assistant_model.h5', 'r') as f:
    # Open a text file in write mode
    with open('assistant_model.txt', 'w') as txt_file:
        # Recursively print all the groups and datasets in the file to the text file
        def print_attrs(name, obj):
            txt_file.write(name + '\n')
            for key, val in obj.attrs.items():
                txt_file.write(f"    {key}: {val}\n")

        f.visititems(print_attrs)

# Close the text file
txt_file.close()


