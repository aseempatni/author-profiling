import os
import graphlab as gl
from bs4 import  BeautifulSoup

BASE_DIR = "../../data/koppel" # NOTE: Update BASE_DIR to your own directory path
class BlogData2SFrameParser(object):
    #Some constants
    ID = "id"
    GENDER = "gender"
    AGE = "age"
    SIGN = "sign"
    POSTS = "posts"
    DATES = "dates"
    INDUSTRY = "industry"

    def __init__(self, xml_files_dir, sframe_outpath):
        """
        Parse all the blog posts XML files in the xml_files_dir and insert them into an SFrame object,
        which is later saved to `sframe_outpath`
        :param xml_files_dir: the directory which contains XML files of the The Blog Authorship Corpus
        :param sframe_outpath: the out path to save the SFrame.
        """
        self._bloggers_data = []


        count = 0
        for p in os.listdir(xml_files_dir):
            if count>1000:
                break
            if p.endswith(".xml"):
                #We parse each XML file and convert it to a dict
                self._bloggers_data.append(self.parse_blog_xml_to_dict("%s%s%s" % (xml_files_dir, os.path.sep, p)))
            count = count+1
        print "Successfully parsed %s blogs" % len(self._bloggers_data)

        # self._bloggers_data is a list of dict which we can easily load to a SFrame object. However, the dict object
        # are loaded into a single column named X1. To create separate column for each dict key we use the unpack function.
        self._sf = gl.SFrame(self._bloggers_data).unpack('X1')

        #Now we can use the rename function in order to remove the X1. prefix from the column names and save the SFrame for later use
        self._sf.rename({c:c.replace("X1.", "") for c in self._sf.column_names()} )
        self._sf.save(sframe_outpath)


    def parse_blog_xml_to_dict(self, path):
        """
        Parse the blog post in the input XML file and return dict with the  blogger's personal information and posts
        :param path: the path of the xml file
        :return: dict with the blogger's personal details and posts
        :rtype: dict
        """
        blogger_dict = {}
        #Extract the blogger personal details from the file name
        blog_id,gender,age,industry, sign = path.split(os.path.sep)[-1].split(".xml")[0].split(".")
        blogger_dict[self.ID] = blog_id
        blogger_dict[self.GENDER] = gender
        blogger_dict[self.AGE] = int(age)
        blogger_dict[self.INDUSTRY] = industry
        blogger_dict[self.SIGN] = sign
        blogger_dict[self.POSTS] = []
        blogger_dict[self.DATES] = []

        #The XML files are not well formatted, so we need to do some hacks.
        s = file(path,"r").read().replace("&nbsp;", " ")

        # First, strip the <Blog> and </Blog> tags at the beginning and end of the document
        s = s.replace("<Blog>", "").replace("</Blog>", "").strip()

        # Now, split the document into individual blog posts by the <date> tag
        for e in s.split("<date>")[1:]:
            # Separate the date stamp from the rest of the post
            date_and_post = e.split("</date>")
            blogger_dict[self.DATES].append(date_and_post[0].strip())
            post = date_and_post[1].replace("<post>","").replace("</post>","").strip()
            post = BeautifulSoup(post).get_text()
            blogger_dict[self.POSTS].append(post)


        if len(blogger_dict[self.DATES]) != len(blogger_dict[self.POSTS]):
            raise Exception("Warning: Mismatch between the number of posts and the number of dates in file %s" % path)

        return blogger_dict
    @property
    def sframe(self):
        return self._sf

sframe_save_path = "blogs.sframe"
b = BlogData2SFrameParser("%s/blogs" % BASE_DIR, sframe_save_path)
sf = b.sframe
