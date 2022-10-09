print( list( x for x in range( 2, int( input( "Pick a number: " ) ) ) if all( map( lambda s: x % s, range( 2, x ) ) ) ) )
