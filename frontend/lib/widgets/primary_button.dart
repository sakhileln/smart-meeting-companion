import 'package:flutter/material.dart';

class PrimaryButton extends StatelessWidget {
  final VoidCallback? onPressed;
  final Widget child;
  final bool fullWidth;
  final EdgeInsetsGeometry? padding;
  final double? width;
  final double height;
  final double borderRadius;
  final Color? backgroundColor;
  final Color? foregroundColor;
  final bool hasShadow;
  final double elevation;

  const PrimaryButton({
    super.key,
    required this.onPressed,
    required this.child,
    this.fullWidth = true,
    this.padding,
    this.width,
    this.height = 48.0,
    this.borderRadius = 12.0,
    this.backgroundColor,
    this.foregroundColor,
    this.hasShadow = true,
    this.elevation = 4.0,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final buttonStyle = ElevatedButton.styleFrom(
      backgroundColor: backgroundColor ?? theme.primaryColor,
      foregroundColor: foregroundColor ?? theme.colorScheme.onPrimary,
      elevation: hasShadow ? elevation : 0,
      padding: padding ?? const EdgeInsets.symmetric(vertical: 12, horizontal: 24),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(borderRadius),
      ),
      minimumSize: Size(
        fullWidth ? double.infinity : (width ?? 0),
        height,
      ),
    );

    return ElevatedButton(
      onPressed: onPressed,
      style: buttonStyle,
      child: child,
    );
  }
}
