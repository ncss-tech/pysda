{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a426de67",
   "metadata": {},
   "outputs": [],
   "source": [
    "#add the location of the pysda package\n",
    "import sys\n",
    "sys.path.insert(1, r'C:\\Users\\Charles.Ferguson\\Documents\\GitHub\\pysda')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "69551470",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the wss module\n",
    "import wss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a6fa7d81",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-34-e8324e3dd4f4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m# shp is default so all we have to do is specify dest (destination)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# which too is optional but if you don't it will go to the current working directory\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mwss\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mavailability\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdest\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mr'C:\\temp\\test'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Documents\\GitHub\\pysda\\wss.py\u001b[0m in \u001b[0;36mavailability\u001b[1;34m(form, dest)\u001b[0m\n\u001b[0;32m     26\u001b[0m         \u001b[0mshp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityShapefile.zip'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m         \u001b[0mname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbasename\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mshp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 28\u001b[1;33m         \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mshp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     29\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m         \u001b[0merr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Unsupported format requested'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mget\u001b[1;34m(url, params, **kwargs)\u001b[0m\n\u001b[0;32m     73\u001b[0m     \"\"\"\n\u001b[0;32m     74\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 75\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'get'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     76\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     77\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(method, url, **kwargs)\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     60\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 61\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     62\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     63\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[0;32m    540\u001b[0m         }\n\u001b[0;32m    541\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 542\u001b[1;33m         \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    543\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    544\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, **kwargs)\u001b[0m\n\u001b[0;32m    695\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    696\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mstream\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 697\u001b[1;33m             \u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcontent\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    698\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    699\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\models.py\u001b[0m in \u001b[0;36mcontent\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    834\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_content\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    835\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 836\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_content\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mb''\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miter_content\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCONTENT_CHUNK_SIZE\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mor\u001b[0m \u001b[1;34mb''\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    837\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    838\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_content_consumed\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\requests\\models.py\u001b[0m in \u001b[0;36mgenerate\u001b[1;34m()\u001b[0m\n\u001b[0;32m    756\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'stream'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    757\u001b[0m                 \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 758\u001b[1;33m                     \u001b[1;32mfor\u001b[0m \u001b[0mchunk\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstream\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchunk_size\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdecode_content\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    759\u001b[0m                         \u001b[1;32myield\u001b[0m \u001b[0mchunk\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    760\u001b[0m                 \u001b[1;32mexcept\u001b[0m \u001b[0mProtocolError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\urllib3\\response.py\u001b[0m in \u001b[0;36mstream\u001b[1;34m(self, amt, decode_content)\u001b[0m\n\u001b[0;32m    574\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    575\u001b[0m             \u001b[1;32mwhile\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mis_fp_closed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_fp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 576\u001b[1;33m                 \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mamt\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mamt\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdecode_content\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdecode_content\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    577\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    578\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\site-packages\\urllib3\\response.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, amt, decode_content, cache_content)\u001b[0m\n\u001b[0;32m    517\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    518\u001b[0m                 \u001b[0mcache_content\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mFalse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 519\u001b[1;33m                 \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_fp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mamt\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mfp_closed\u001b[0m \u001b[1;32melse\u001b[0m \u001b[1;34mb\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    520\u001b[0m                 if (\n\u001b[0;32m    521\u001b[0m                     \u001b[0mamt\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[1;36m0\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\http\\client.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, amt)\u001b[0m\n\u001b[0;32m    463\u001b[0m             \u001b[1;31m# Amount is given, implement using readinto\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    464\u001b[0m             \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbytearray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mamt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 465\u001b[1;33m             \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadinto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    466\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mmemoryview\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtobytes\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    467\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\http\\client.py\u001b[0m in \u001b[0;36mreadinto\u001b[1;34m(self, b)\u001b[0m\n\u001b[0;32m    507\u001b[0m         \u001b[1;31m# connection, and the user is reading more bytes than will be provided\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    508\u001b[0m         \u001b[1;31m# (for example, reading in 1k chunks)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 509\u001b[1;33m         \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadinto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    510\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mn\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    511\u001b[0m             \u001b[1;31m# Ideally, we would raise IncompleteRead if the content-length\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\socket.py\u001b[0m in \u001b[0;36mreadinto\u001b[1;34m(self, b)\u001b[0m\n\u001b[0;32m    587\u001b[0m         \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    588\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 589\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_sock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    590\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    591\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_timeout_occurred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\ssl.py\u001b[0m in \u001b[0;36mrecv_into\u001b[1;34m(self, buffer, nbytes, flags)\u001b[0m\n\u001b[0;32m   1069\u001b[0m                   \u001b[1;34m\"non-zero flags not allowed in calls to recv_into() on %s\"\u001b[0m \u001b[1;33m%\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1070\u001b[0m                   self.__class__)\n\u001b[1;32m-> 1071\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnbytes\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1072\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1073\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0msuper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbuffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnbytes\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\proclone283\\lib\\ssl.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, len, buffer)\u001b[0m\n\u001b[0;32m    927\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    928\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mbuffer\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 929\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    930\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    931\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "# lets step through functions\n",
    "# first get the soil data availability shapefile(zipped)\n",
    "# possible formats are shp (zipped), pdf, or jpg.\n",
    "# shp is default so all we have to do is specify dest (destination)\n",
    "# which too is optional but if you don't it will go to the current working directory\n",
    "wss.availability(dest = r'C:\\temp\\test')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c1892dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# next let's get a data frame that shows\n",
    "# the possible soil survey todownload.\n",
    "# ultimately we need the url but we have \n",
    "# to associate the url to a SSA\n",
    "# let's get them all first\n",
    "df = wss.ssurgo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08c0eb63",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c551792a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# most people don't need all the survey areas\n",
    "# filters exist state or search on areaname\n",
    "# let's do state first\n",
    "deleware = wss.ssurgo(state = 'DE')\n",
    "\n",
    "# deleware only has 3 ares so we will\n",
    "# see that the filter works\n",
    "deleware.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13670096",
   "metadata": {},
   "outputs": [],
   "source": [
    "# now let's filter on areaname\n",
    "# and find all surveys that have\n",
    "# hamilton in the areaname\n",
    "search = wss.ssurgo(search = 'hamilton')\n",
    "\n",
    "search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f16b5b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# since we have a pandas data frame\n",
    "# lets subset it so we only grab 2 areas\n",
    "# for example purposes\n",
    "import re\n",
    "search = search[search['areaname'].str.contains('ohi|florida', flags = re.IGNORECASE)]\n",
    "search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09e25e38",
   "metadata": {},
   "outputs": [],
   "source": [
    "# now that we have just a couple\n",
    "# let's download them. we will\n",
    "# choose to unzip and rename to the\n",
    "# old style ssurgo naming convention\n",
    "# note: frame is ideally a pandas data frame\n",
    "# however an iterable of valid URLs is acceptable\n",
    "wss.download(frame=search, dest=r'C:\\temp\\test', unpack=True, rename=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "446dcb35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# here we can see the we have, \n",
    "# into the C:\\temp\\test folder\n",
    "# 1. downloaded the SoilData Availability Shapefile\n",
    "# 2. downloaded 2 soil surveys, unzipped them, and renamed\n",
    "import os\n",
    "os.listdir(r'C:\\temp\\test')\n",
    " \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
