from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse

from .models import RGB, RGBA


def hello_world(request):
    return HttpResponse("Hello world")


def index(request: HttpRequest):
    def get_colour(key: str):
        request_item: int = None

        try:
            request_item = int(request.GET[key])
        except:
            return 69

        return request_item

    try:
        r = get_colour("r")
        g = get_colour("g")
        b = get_colour("b")
        a = get_colour("a")

        colour = RGBA(r=r, g=g, b=b, a=a)
        complementary_colour = _complementary_colour_factory(colour)

        template = loader.get_template("complementary/index.html")
        context = {"colour": colour, "complementary_colour": complementary_colour}
        # context = {"colour": colour}
    except:
        raise Http404("Issue getting complentary value")

    return HttpResponse(template.render(context, request))


def _complementary_colour_factory(colour: RGB) -> RGBA:
    """SEE
    https://stackoverflow.com/questions/40233986/python-is-there-a-function-or-formula-to-find-the-complementary-colour-of-a-rgb
    """

    def complementary_primary(primary: int, delta: int) -> int:
        return delta - primary

    def alpha():
        if hasattr(colour, "a"):
            return colour.a
        else:
            return 255

    min_primary = min(colour.r, colour.g, colour.b)
    max_primary = max(colour.r, colour.g, colour.b)

    min_max_sum = min_primary + max_primary

    complementary = RGBA(
        r=complementary_primary(colour.r, min_max_sum),
        g=complementary_primary(colour.g, min_max_sum),
        b=complementary_primary(colour.b, min_max_sum),
        a=alpha()
    )

    return complementary
