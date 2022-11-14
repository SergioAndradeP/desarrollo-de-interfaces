package com.example.mycatalog;

import android.content.ActivityNotFoundException;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener{

    private Context context=this;
    private DrawerLayout drawerLayout;
    private NavigationView navigationView;
    private Toolbar toolbar;
    private Menu menu;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        drawerLayout=findViewById(R.id.drawer_layout);
        navigationView=findViewById(R.id.navigator_layout);
        toolbar=findViewById(R.id.toolbar_id);
        setSupportActionBar(toolbar);

        menu=navigationView.getMenu();
        navigationView.getHeaderView(0);
        navigationView.bringToFront();


        ActionBarDrawerToggle toggle= new ActionBarDrawerToggle( this, drawerLayout, toolbar, R.string.navigator_open, R.string.navigator_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
        navigationView.setNavigationItemSelectedListener(this);
        navigationView.setCheckedItem(R.id.catalog);
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        switch(item.getItemId()){
            case R.id.catalog:
                Fragment fragmentCatalog = new CatalogFragment();
                getSupportFragmentManager().beginTransaction().replace(R.id.frameLayout, fragmentCatalog).commit();
                break;
            case R.id.about:
                Fragment fragmentAbout = new AboutFragment();
                getSupportFragmentManager().beginTransaction().replace(R.id.frameLayout, fragmentAbout).commit();
                break;
        }
        return false;
    }
}