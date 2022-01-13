# Egypt_AbnormalBehaviour_ITIGP
-------------------------------------------------------------------------
This app is used to to determine the abnormal crowed behavior in Egypt street by taking 
the video and do some processing to prepare it to fit into the Model.

#### Accuracy on Training Data is : 99.1% 
#### Accuracy on Test Data is : 97.5 %
#### Data : was manually Detected and Labeled from camera videos in Egypt street 
![image](https://user-images.githubusercontent.com/83990621/147882194-1e948051-604f-42bd-9a03-50cb67f03c86.png)
![image](https://user-images.githubusercontent.com/83990621/147882206-1ff6b001-bf57-41c1-b5c2-8c2758da9e46.png)

The Model was an implementaion from research paper, you can find it in that [link](https://link.springer.com/article/10.1007/s42979-020-00207-x)

### Research:
---------------------
![image](https://user-images.githubusercontent.com/83990621/147882213-d36d7c6d-2810-4651-812c-4242fd9a4d85.png)

• Halder, R., Chatterjee, R. CNN-BiLSTM Model for Violence Detection in Smart Surveillance. 
SN COMPUT. SCI. 1, 201 (2020).

• School of Computer Engineering, KIIT Deemed to be University, Bhubaneswar 751024, Odisha, India.
-------------------------
### Challenges:
1- Collecting new Data with different situation and locations.
2- Increase the input data or training many times to make the model to learn more.


### Enhancements:
1- Change the number of epochs from 10 to 12.
2- Make a callback of reducing Learning rate of the SGD optimizers to reduce the overshooting
3- Try to use Different Frame rate per second
![image](https://user-images.githubusercontent.com/83990621/147882238-970a412f-c846-49e4-b694-f7a4ec137bfb.png)


------------------------------------------------------------------------------------------------------------------------
### Installation
Requirements-Python 3.9 
pip install -r /path/to/requirements.txt
---------------------------------------------------------------------------
### Run The App:
Run File application.py 
![image](https://user-images.githubusercontent.com/83990621/147882270-acd446ad-22f6-4052-b559-cf1d7318db73.png)

