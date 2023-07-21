const generatePDF=async(name)=>{
    const {PDFDocument , rgb }=PDFLib;
    const exBytes= await fetch("/static/img/Certificate.pdf").then((res)=>{
        return res.arrayBuffer();
    })
    const exFonts= await fetch("/static/fonts/DancingScript-Regular.ttf").then((res)=>{
        return res.arrayBuffer();
    })
    const pdfDoc=await PDFDocument.load(exBytes)

    pdfDoc.registerFontkit(fontkit)
    const myfont=await pdfDoc.embedFont(exFonts)
    const pages=pdfDoc.getPages()
    const page=pages[0]
    page.drawText(name,{
        x:250,y:300,size:50,font:myfont
    })

    const uri= await pdfDoc.saveAsBase64({dataUri:true})
    document.querySelector('#donateCerticate').src =uri
}
generatePDF("Dipanshu Khandait")