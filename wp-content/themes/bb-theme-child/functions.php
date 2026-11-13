<?php

// Defines
define( 'FL_CHILD_THEME_DIR', get_stylesheet_directory() );
define( 'FL_CHILD_THEME_URL', get_stylesheet_directory_uri() );

// Classes
require_once 'classes/class-fl-child-theme.php';

// Black & Brass redesign (2026). Scoped to pages flagged with the _ja26 meta.
if ( file_exists( FL_CHILD_THEME_DIR . '/classes/class-ja-redesign.php' ) ) {
	require_once FL_CHILD_THEME_DIR . '/classes/class-ja-redesign.php';
}

// Actions
add_action( 'wp_enqueue_scripts', 'FLChildTheme::enqueue_scripts', 1000 );
