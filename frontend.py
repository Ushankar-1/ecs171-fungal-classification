import pickle
import streamlit as st


def fungus_input_converter(image):

    # Here, need to reshape input image to numpy array
    # like how dataset is preprocessed, but with only one input  
    
    # TODO: figure out how to handle color. Do we need to wipe RBG data for all inputs?
    # that depends on how model works
    print('hi')

def fungus_prediction(inputData):

    # Import model, run predictions on it    
    
    loaded_model = pickle.load(open('FILEPATH GOES HERE', 'rb'))
    # TODO: enter filepath relative to this file. Where will final model be saved?

    prediction = loaded_model.predict(inputData)
    
    if(prediction[0] == 1): # Assumes predictive algorithm returns 1, 2, 3, 5, or 6
        return 'This fungi is in class H1'
    elif(prediction[0] == 2): # Assumes predictive algorithm returns 1, 2, 3, 5, or 6
        return 'This fungi is in class H2'
    elif(prediction[0] == 3): # Assumes predictive algorithm returns 1, 2, 3, 5, or 6
        return 'This fungi is in class H3'
    elif(prediction[0] == 5): # Assumes predictive algorithm returns 1, 2, 3, 5, or 6
        return 'This fungi is in class H5'
    elif(prediction[0] == 6): #Assumes predictive algorithm returns 1, 2, 3, 5, or 6
        return 'This fungi is in class H6'
    else:
        return 'Classification error'

def main():
    
    st.title('Fungi classifier')
    
    #INSERT IMAGE INPUT UPLOAD HERE
    inputImage = st.file_uploader('Upload a.JPG microscopic image of a fungal infection here:', type=['jpg'])
    inputData = fungus_input_converter(inputImage)
    
    classification = ''
    
    if st.button('Classify!'):
        classification = fungus_prediction(inputData)
        
    st.success(classification)
    


if __name__ == '__main__':
        main()





