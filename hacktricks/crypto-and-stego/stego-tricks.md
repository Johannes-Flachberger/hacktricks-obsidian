# Stego Tricks


## **Extracting Data from Files**

### **Binwalk**

A tool for searching binary files for embedded hidden files and data. It's installed via `apt` and its source is available on [[https://github.com/ReFirmLabs/binwalk|GitHub]].

```bash
binwalk file # Displays the embedded data
binwalk -e file # Extracts the data
binwalk --dd ".*" file # Extracts all data
```
```
### **Foremost**

Recovers files based on their headers and footers, useful for png images. Installed via `apt` with its source on [[https://github.com/korczis/foremost|GitHub]].

```bash
foremost -i file # Extracts data
```
```
### **Exiftool**

Helps to view file metadata, available [[https://www.sno.phy.queensu.ca/~phil/exiftool/|here]].

```bash
exiftool file # Shows the metadata
```
```
### **Exiv2**

Similar to exiftool, for metadata viewing. Installable via `apt`, source on [[https://github.com/Exiv2/exiv2), and has an [official website](http://www.exiv2.org/|GitHub]].

```bash
exiv2 file # Shows the metadata
```
```
### **File**

Identify the type of file you're dealing with.

### **Strings**

Extracts readable strings from files, using various encoding settings to filter the output.

```bash
strings -n 6 file # Extracts strings with a minimum length of 6
strings -n 6 file | head -n 20 # First 20 strings
strings -n 6 file | tail -n 20 # Last 20 strings
strings -e s -n 6 file # 7bit strings
strings -e S -n 6 file # 8bit strings
strings -e l -n 6 file # 16bit strings (little-endian)
strings -e b -n 6 file # 16bit strings (big-endian)
strings -e L -n 6 file # 32bit strings (little-endian)
strings -e B -n 6 file # 32bit strings (big-endian)
```
```
### **Comparison (cmp)**

Useful for comparing a modified file with its original version found online.

```bash
cmp original.jpg stego.jpg -b -l
```
```
## **Extracting Hidden Data in Text**

### **Hidden Data in Spaces**

Invisible characters in seemingly empty spaces may hide information. To extract this data, visit [[https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder|https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder]].

## **Extracting Data from Images**

### **Identifying Image Details with GraphicMagick**

[[https://imagemagick.org/script/download.php|GraphicMagick]] serves to determine image file types and identify potential corruption. Execute the command below to inspect an image:

```bash
./magick identify -verbose stego.jpg
```
```
To attempt repair on a damaged image, adding a metadata comment might help:

```bash
./magick mogrify -set comment 'Extraneous bytes removed' stego.jpg
```
```
### **Steghide for Data Concealment**

Steghide facilitates hiding data within `JPEG, BMP, WAV, and AU` files, capable of embedding and extracting encrypted data. Installation is straightforward using `apt`, and its [[https://github.com/StefanoDeVuono/steghide|source code is available on GitHub]].

**Commands:**

- `steghide info file` reveals if a file contains hidden data.
- `steghide extract -sf file [--passphrase password]` extracts the hidden data, password optional.

For web-based extraction, visit [[https://futureboy.us/stegano/decinput.html|this website]].

**Bruteforce Attack with Stegcracker:**

- To attempt password cracking on Steghide, use [[https://github.com/Paradoxis/StegCracker.git|stegcracker]] as follows:

```bash
stegcracker <file> [<wordlist>]
```
```
### **zsteg for PNG and BMP Files**

zsteg specializes in uncovering hidden data in PNG and BMP files. Installation is done via `gem install zsteg`, with its [[https://github.com/zed-0xff/zsteg|source on GitHub]].

**Commands:**

- `zsteg -a file` applies all detection methods on a file.
- `zsteg -E file` specifies a payload for data extraction.

### **StegoVeritas and Stegsolve**

**stegoVeritas** checks metadata, performs image transformations, and applies LSB brute forcing among other features. Use `stegoveritas.py -h` for a full list of options and `stegoveritas.py stego.jpg` to execute all checks.

**Stegsolve** applies various color filters to reveal hidden texts or messages within images. It's available on [[https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve|GitHub]].

### **FFT for Hidden Content Detection**

Fast Fourier Transform (FFT) techniques can unveil concealed content in images. Useful resources include:

- [[http://bigwww.epfl.ch/demo/ip/demos/FFT/|EPFL Demo]]
- [[https://www.ejectamenta.com/Fourifier-fullscreen/|Ejectamenta]]
- [[https://github.com/0xcomposure/FFTStegPic|FFTStegPic on GitHub]]

### **Stegpy for Audio and Image Files**

Stegpy allows embedding information into image and audio files, supporting formats like PNG, BMP, GIF, WebP, and WAV. It's available on [[https://github.com/dhsdshdhk/stegpy|GitHub]].

### **Pngcheck for PNG File Analysis**

To analyze PNG files or to validate their authenticity, use:

```bash
apt-get install pngcheck
pngcheck stego.png
```
```
### **Additional Tools for Image Analysis**

For further exploration, consider visiting:

- [[http://magiceye.ecksdee.co.uk/|Magic Eye Solver]]
- [[https://29a.ch/sandbox/2012/imageerrorlevelanalysis/|Image Error Level Analysis]]
- [[https://github.com/resurrecting-open-source-projects/outguess|Outguess]]
- [[https://www.openstego.com/|OpenStego]]
- [[https://diit.sourceforge.net/|DIIT]]

## **Extracting Data from Audios**

**Audio steganography** offers a unique method to conceal information within sound files. Different tools are utilized for embedding or retrieving hidden content.

### **Steghide (JPEG, BMP, WAV, AU)**

Steghide is a versatile tool designed for hiding data in JPEG, BMP, WAV, and AU files. Detailed instructions are provided in the [[stego-tricks.md#steghide|stego tricks documentation]].

### **Stegpy (PNG, BMP, GIF, WebP, WAV)**

This tool is compatible with a variety of formats including PNG, BMP, GIF, WebP, and WAV. For more information, refer to [[stego-tricks.md#stegpy-png-bmp-gif-webp-wav|Stegpy's section]].

### **ffmpeg**

ffmpeg is crucial for assessing the integrity of audio files, highlighting detailed information and pinpointing any discrepancies.

```bash
ffmpeg -v info -i stego.mp3 -f null -
```
```
### **WavSteg (WAV)**

WavSteg excels in concealing and extracting data within WAV files using the least significant bit strategy. It is accessible on [[https://github.com/ragibson/Steganography#WavSteg|GitHub]]. Commands include:

```bash
python3 WavSteg.py -r -b 1 -s soundfile -o outputfile

python3 WavSteg.py -r -b 2 -s soundfile -o outputfile
```
```
### **Deepsound**

Deepsound allows for the encryption and detection of information within sound files using AES-256. It can be downloaded from [[http://jpinsoft.net/deepsound/download.aspx|the official page]].

### **Sonic Visualizer**

An invaluable tool for visual and analytical inspection of audio files, Sonic Visualizer can unveil hidden elements undetectable by other means. Visit the [[https://www.sonicvisualiser.org/|official website]] for more.

### **DTMF Tones - Dial Tones**

Detecting DTMF tones in audio files can be achieved through online tools such as [[https://unframework.github.io/dtmf-detect/) and [DialABC](http://dialabc.com/sound/detect/index.html|this DTMF detector]].

## **Other Techniques**

### **Binary Length SQRT - QR Code**

Binary data that squares to a whole number might represent a QR code. Use this snippet to check:

```python
import math
math.sqrt(2500) #50
```
```
For binary to image conversion, check [[https://www.dcode.fr/binary-image). To read QR codes, use [this online barcode reader](https://online-barcode-reader.inliteresearch.com/|dcode]].

### **Braille Translation**

For translating Braille, the [[https://www.branah.com/braille-translator|Branah Braille Translator]] is an excellent resource.

## **References**

- [[https://0xrick.github.io/lists/stego/|**https://0xrick.github.io/lists/stego/**]]
- [[https://github.com/DominicBreuker/stego-toolkit|**https://github.com/DominicBreuker/stego-toolkit**]]



