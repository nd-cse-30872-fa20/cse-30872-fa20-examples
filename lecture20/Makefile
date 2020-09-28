CXX=		g++
CXXFLAGS=	-g -std=gnu++11 -Wall
LD=		g++
LDFLAGS=

all:		program

program:	main.o graph.o
	$(LD) $(LDFLAGS) -o $@ $^

%.o:		%.c graph.h
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f program *.o
