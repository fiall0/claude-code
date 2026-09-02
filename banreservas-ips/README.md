# Banreservas · Pago Instantáneo RD — kit de pantallas para Figma

Prototipo HTML de alta fidelidad del **sistema de pagos inmediatos (IPS)** dentro del Internet
Banking de Banreservas. Toma la identidad visual del portal actual (barra superior blanca, menú
lateral cyan con ítem activo naranja, tarjetas blancas sobre gris, paneles azul institucional) y
modela la experiencia sobre los IPS de referencia de la región: **Bre-B** (Colombia), **Pix**
(Brasil), **DiMo/SPEI** (México) y **Transfer 3.0** (Argentina).

- `index.html` — archivo único con **59 frames**, autocontenido (CSS embebido, iconos y QR en SVG).
- `build.py` — generador. Edita aquí y regenera con `python3 build.py`.

## Cómo llevarlo a Figma

1. Instala el plugin **html.to.design** (Figma → Plugins → html.to.design).
2. Pestaña *Code / File* → pega el contenido de `index.html` o sube el archivo. Ancho de importación: **1440 px**.
3. Cada tarjeta con etiqueta (`B-01`, `D-03`, …) entra como frame independiente, con auto-layout,
   textos editables e iconos como vectores.
4. Los colores están definidos como variables CSS en `:root`; conviértelos a *variables/estilos* de
   Figma para tener el tema completo.

Alternativa: publicar el archivo en cualquier URL y usar la importación por link, que suele
conservar mejor la jerarquía de capas.

## Contenido (59 frames)

| Grupo | Frames | Qué cubre |
|---|---|---|
| **A · Fundamentos** | A-01 … A-04 | Portada, tokens de color/tipografía, librería de componentes, mapa de flujos |
| **B · Entrada** | B-01 … B-03 | Inicio con el módulo IPS, menú *Transferir* desplegado, hub del producto |
| **C · Mis Alias** | C-01 … C-12 | Educativo, T&C, tipo de alias, OTP, cuenta asociada, confirmación, éxito, listado, detalle/edición, portabilidad, alias `@` personalizado |
| **D · Enviar pago** | D-01 … D-13 | Destino, resolución de alias, confirmación de nombre, monto, revisión, 2FA (push/OTP/token), aprobación móvil, procesando, comprobante, matriz de errores, autenticación reforzada |
| **E · Solicitar pago** | E-01 … E-09 | Destinatario, monto y vencimiento, revisión, compartir (enlace/QR), bandejas enviadas y recibidas, detalle, pago de una solicitud, rechazo con motivo |
| **F · Pagar con QR** | F-01 … F-09 | Hub, opciones de lectura, escáner, QR estático (digitar monto), QR dinámico con vencimiento, autenticación, comprobante, *mi QR* de cobro, errores |
| **G · Seguridad y post-venta** | G-01 … G-09 | Panel de seguridad, límites, dispositivos y sesiones, métodos de autenticación, alertas, alias bloqueados/reportes, movimientos, devolución/reclamación, estados vacíos y microcopy |

## Modelo funcional (alias)

Cinco tipos de alias, uno por tipo y hasta 5 por cliente, únicos a nivel nacional y resueltos contra
un **Directorio Centralizado de Alias**: celular, correo, cédula, alias personalizado `@usuario` y
RNC para comercios. Cada alias apunta a **una sola cuenta en DOP**; incluye portabilidad entre
entidades con ventana de 5 días, igual que el reclamo de llaves de Bre-B.

## Controles de seguridad representados

Los que hoy aplican los bancos a transferencias, incorporados como pantallas reales y no como texto:

- **Doble factor por operación**: aprobación push con biometría en la app, token blando, OTP SMS/correo, passkey WebAuthn.
- **Confirmación del nombre del beneficiario** enmascarado antes de autorizar (control anti-error y anti-suplantación).
- **Límites** por transacción / diario / mensual, con **enfriamiento de 24 h** para los aumentos y tope reducido para beneficiarios nuevos.
- **Autenticación reforzada (step-up)** disparada por score de riesgo: beneficiario nuevo, monto atípico, dispositivo o geolocalización inusual.
- **Dispositivos de confianza**, cierre remoto de sesiones, expiración por inactividad y bloqueo tras 3 intentos fallidos.
- **Sello anti-phishing** personal en correos y SMS, y aviso permanente de que el banco nunca pide claves ni OTP.
- **Reporte y bloqueo de alias**, señal de riesgo compartida entre entidades y **modo seguro** que bloquea todos los pagos salientes.
- **QR EMVCo verificado**: validación de firma, comercio activo, vigencia del código dinámico y monto no alterable.
- **Trazabilidad**: comprobante con referencia propia y del sistema, QR de verificación, y canal de **devolución/reclamación** con motivos tipificados.
- Irrevocabilidad advertida en todos los puntos de decisión, con reversa automática documentada cuando el receptor rechaza.

> Nota: “Pago Instantáneo RD” y el nombre del directorio son marcas de trabajo del prototipo, no
> denominaciones oficiales. Los saldos, nombres, referencias y RNC son ficticios.
