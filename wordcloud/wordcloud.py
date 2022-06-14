import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# def _upload():
#
#     _upload_widget = fileupload.FileUploadWidget()
#
#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()
#
#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)
#
# _upload()

file_contents = "This means that bob refers to an object with type Turtle as defined in module turtle.mainloop tells the window to wait for the user to do something, although in this case there’s not much for the user to do except close the window.Once you create a Turtle, you can call a method to move it around the window. A method is similar to a function, but it uses slightly different syntax. For example, to move the turtle forward: bob.fd(100) The method, fd, is associated with the turtle object we’re calling bob. Calling a method is like making a request: you are asking bob to move forward.The argument of fd is a distance in pixels, so the actual size depends on your display.Other methods you can call on a Turtle are bk to move backward, lt for left turn, and rt right turn. The argument for lt and rt is an angle in degrees. Also, each Turtle is holding a pen, which is either down or up; if the pen is down, the Turtle leaves a trail when it moves. The methods pu and pd stand for “pen up” and “pen down”. To draw a right angle, add these lines to the program (after creating bob and before calling mainloop): bob.fd(100) This is the simplest use of the for statement; we will see more later. But that should be enough to let you rewrite your square-drawing program. Don’t go on until you do. Here is a for statement that draws a square: or i in range(4): bob.fd(100) bob.lt(90) The syntax of a for statement is similar to a function definition. It has a header that ends with a colon and an indented body. The body can contain any number of statements. A for statement is also called a loop because the flow of execution runs through the body and then loops back to the top. In this case, it runs the body four times. This version is actually a little different from the previous square-drawing code because it makes another turn after drawing the last side of the square. The extra turn takes more time, but it simplifies the code if we do the same thing every time through the loop. This version also has the effect of leaving the turtle back in the starting position, facing in the starting direction. 4.3 Exercises The following is a series of exercises using the turtle module. They are meant to be fun, but they have a point, too. While you are working on them, think about what the point is. The following sections have solutions to the exercises, so don’t look until you have finished (or at least tried). 1. Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square. Write a function call that passes bob as an argument to square, and then run the program again. 2. Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument. Run  he program again. Test your program with a range of values for length. 3. Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees."

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    file_contents = file_contents.split(' ')
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just", ""]

    for i in range(len(file_contents)):
        word = file_contents[i]
        if not word.isalpha():
            sent = ''
            for char in word:
                if char.isalpha():
                    sent += char

            file_contents[i] = sent
        file_contents[i] = file_contents[i].lower()

    for word in uninteresting_words:
        if word in file_contents:
            try:
                while True:
                    file_contents.remove(word)
            except ValueError:
                pass

    dic = {}
    for word in file_contents:
        if word not in dic.keys():
            dic[word] = file_contents.count(word)

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dic)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()