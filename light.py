glMatrixMode (GL_PROJECTION);
glLoadIdentity();
glFrustum(-0.1,0.1, -0.1,0.1, 0.2,1000);
glMatrixMode (GL_MODELVIEW);
glLoadIdentity();