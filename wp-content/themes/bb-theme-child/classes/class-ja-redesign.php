<?php
/**
 * Jamil Ahmed: Black & Brass redesign.
 *
 * Everything here is scoped to pages that carry the `_ja26` post meta, so the
 * rest of the live site keeps its current look until launch. To roll the design
 * out site-wide later, make JA_Redesign::is_active() return true everywhere.
 */

defined( 'ABSPATH' ) || exit;

final class JA_Redesign {

	const VERSION = '1.0.0';

	public static function init() {
		add_filter( 'body_class', array( __CLASS__, 'body_class' ) );
		add_action( 'wp_enqueue_scripts', array( __CLASS__, 'enqueue' ), 1001 );
	}

	/**
	 * Whether the current request renders a redesigned page.
	 */
	public static function is_active() {
		if ( is_admin() ) {
			return false;
		}
		$id = get_queried_object_id();
		return $id && is_singular() && (bool) get_post_meta( $id, '_ja26', true );
	}

	public static function body_class( $classes ) {
		if ( self::is_active() ) {
			$classes[] = 'ja26';
		}
		return $classes;
	}

	public static function enqueue() {
		if ( ! self::is_active() ) {
			return;
		}
		wp_enqueue_style(
			'ja26-fonts',
			'https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500&display=swap',
			array(),
			null
		);
		$file = FL_CHILD_THEME_DIR . '/assets/css/ja26.css';
		wp_enqueue_style(
			'ja26',
			FL_CHILD_THEME_URL . '/assets/css/ja26.css',
			array( 'ja26-fonts' ),
			file_exists( $file ) ? (string) filemtime( $file ) : self::VERSION
		);
	}
}

JA_Redesign::init();
