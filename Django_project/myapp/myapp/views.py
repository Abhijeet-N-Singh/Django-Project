from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>Hello All Welcome</h1>
                            <h2> To My First Django Project</h2>
                            <ul>
                                <li><a href="/">Home<a></li>
                                <li><a href="/Contactus">Contactus<a></li>
                                <li><a href="/ProductList">ProductList<a></li>
                                <li><a href="/Product">Product<a></li>
                                <li><a href="/Aboutus">Aboutus<a></li>
                        
                            </ul>
                        
                        ''')


def Aboutus(request):
    return HttpResponse('''

            hello I am About us   
                        <ul>
                                <li><a href="/">Home<a></li>
                                
                                <li><a href="/Contactus">Contactus<a></li>
                                <li><a href="/ProductList">ProductList<a></li>
                                <li><a href="/Product">Product<a></li>
                                <li><a href="/Aboutus">Aboutus<a></li>
                        
                            </ul>  
''')


def Contactus(request):
    return HttpResponse('''

            hello I am contactus
                        <ul>
                                <li><a href="/">Home<a></li>
                                
                                <li><a href="/Contactus">Contactus<a></li>
                                <li><a href="/ProductList">ProductList<a></li>
                                <li><a href="/Product">Product<a></li>
                                <li><a href="/Aboutus">Aboutus<a></li>
                        
                            </ul>
''')

def ProductList(request):
    return HttpResponse('''

            hello I am productlist   
                        <ul>
                                <li><a href="/">Home<a></li>
                                
                                <li><a href="/Contactus">Contactus<a></li>
                                <li><a href="/ProductList">ProductList<a></li>
                                <li><a href="/Product">Product<a></li>
                                <li><a href="/Aboutus">Aboutus<a></li>
                        
                            </ul>  
''')

def Product(request):
    return HttpResponse('''

            hello I am product     
                        <ul>
                                <li><a href="/">Home<a></li>
                                
                                <li><a href="/Contactus">Contactus<a></li>
                                <li><a href="/ProductList">ProductList<a></li>
                                <li><a href="/Product">Product<a></li>
                                <li><a href="/Aboutus">Aboutus<a></li>
                        
                            </ul>
''')