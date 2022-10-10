print( list( x for x in range( 2, int( input( "Pick a number: " ) ) + 1 ) if all( map( lambda s: x % s, range( 2, x ) ) ) ) )
