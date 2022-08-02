import os 
import shutil
import zipfile
from str2img import str2img
from titleform import titleform
import shutil

t=input('title:')
creator=input('auother: ')
str2img(t)
titleform()
cover='cover.jpg'
d = os.walk(r"./") 
g = os.walk(r"./") 
for path,dir_list,file_list in d:  
    i=1
    for file_name in file_list: 
        if os.path.splitext(file_name)[1]=='.txt':
            os.rename(file_name,'ch'+str(i).zfill(5)+'.txt')
            i+=1 
titelist=[]
filenamelist=[]
os.mkdir('./'+t)
os.mkdir('./'+t+'/OEBPS')
os.mkdir('./'+t+'/META-INF')
shutil.copyfile('./'+cover, './'+t+'/OEBPS/'+cover)
with open('./'+t+'/mimetype','w',encoding="UTF-8") as f:
    f.write('application/epub+zip')

for path,dir_list,file_list in g:  
    for file_name in file_list: 
        if os.path.splitext(file_name)[1]=='.txt':
            title=str()
            filenamelist.append(file_name.split('.')[0]+".html")
            data=[]
            print('converting:'+file_name)
            with open(file_name, "r",encoding='UTF-8') as f:
                title = f.readline()
                titelist.append(title)
            with open(file_name, "r",encoding='UTF-8') as f:
                data = f.readlines()
            with open('./'+t+'/OEBPS/'+file_name.split('.')[0]+".html","w",encoding='utf-8') as f:
                f.write('<html xmlns="http://www.w3.org/1999/xhtml"><head>')
                f.write('<title>'+title+'</title>')
                f.write('</head>')
                f.write('<body>')
                for line in data:
                    f.write('<p>'+line+'</p>')
                f.write('</body></html>')
            print('convert '+file_name+' end')
with open('./'+t+'/OEBPS/toc.ncx','w',encoding="UTF-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    f.write('<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">')
    f.write('<ncx version="2005-1" xmlns="http://www.daisy.org/z3986/2005/ncx/">')
    f.write('<head>')
    f.write('<meta name="dtb:uid" content=""/>')
    f.write('<meta name="dtb:depth" content="1"/>')
    f.write('<meta name="dtb:totalPageCount" content="0"/>')
    f.write('<meta name="dtb:maxPageNumber" content="0"/>')
    f.write('</head>')
    f.write('<docTitle>')
    f.write('<text>'+str(t)+'</text>')
    f.write('</docTitle>')
    f.write('<navMap>')
    i=0
    for tt in titelist:
        f.write('<navPoint id="navPoint-'+str(i)+'" playOrder="'+str(i)+'"><navLabel><text>'+str(titelist[i])+'</text></navLabel><content src="'+filenamelist[i]+'"/></navPoint>')
        i+=1
    f.write('</navMap></ncx>')

with open('./'+t+'/OEBPS/content.opf','w',encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8" ?><package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uuid_id" version="2.0"><metadata xmlns:opf="http://www.idpf.org/2007/opf" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uuid_id" opf:scheme="uuid">{7B48F6EB-2D1A-46DC-AA51-07EE88454151}</dc:identifier><dc:title>'+str(t))
    f.write('</dc:title><dc:creator opf:role="aut">'+str(creator))
    f.write('</dc:creator><dc:contributor opf:role="bkp">sk</dc:contributor><dc:publisher>uread 1.35.866 简体版</dc:publisher>')
    f.write('<dc:subject></dc:subject><dc:language>zh</dc:language><dc:description></dc:description>')
    f.write('<meta name="cover" content="cover"/></metadata><manifest>')
    f.write('<item href="toc.ncx" media-type="application/x-dtbncx+xml" id="ncx"/>')
    f.write('<item href="'+str(cover)+'" id="cover" media-type="image/'+cover.split('.')[1]+'"/>')
    f.write('<item href="coverpage.xhtml" id="coverpage" media-type="application/xhtml+xml"/>')
    i=0
    k=[]
    for fn in filenamelist:
        k.append(filenamelist[i].split('.')[0])
        f.write('<item href="'+str(filenamelist[i])+'" id="'+filenamelist[i].split('.')[0]+'" media-type="application/xhtml+xml"/>')
        i+=1
    f.write('</manifest><spine toc="ncx">')
    for j in k:
        f.write('<itemref idref="'+str(j)+'"/>')
    f.write('</spine></package>')

with open('./'+t+'/OEBPS/coverpage.xhtml','w',encoding='utf-8') as f:
    f.write('<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>cover</title></head><body>')
    f.write('<div><img src="'+str(cover)+'" alt="cover" /></div>')
    f.write('</body></html>')

with open('./'+t+'/META-INF/container.xml','w',encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="utf-8" ?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
zip = zipfile.ZipFile(t+'.epub', "w", zipfile.ZIP_DEFLATED)
for path, dirnames, filenames in os.walk('./'+t):
    for filename in filenames:
        zip.write(os.path.join(path, filename))
zip.close()
clean=os.walk(r"./") 
for path,dir_list,file_list in clean:  
    for file_name in file_list: 
        if os.path.splitext(file_name)[1]=='.txt':
            os.remove(file_name)
shutil.rmtree('./'+t)