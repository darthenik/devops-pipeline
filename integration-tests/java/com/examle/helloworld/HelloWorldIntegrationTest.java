package com.example.helloworld;

import org.junit.Test;
import static org.junit.Assert.assertNotNull;

public class HelloWorldIntegrationTest {
    @Test
    public void testIntegration() {
        HelloWorld helloWorld = new HelloWorld();
        assertNotNull(helloWorld);
    }
}
