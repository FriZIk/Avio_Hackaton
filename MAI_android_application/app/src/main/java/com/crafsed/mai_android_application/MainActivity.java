package com.crafsed.mai_android_application;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity implements LoadFragment.MListener {

    private static final int REQUEST_CODE = 1;
    LoadFragment mLoadFragment;
    SettingsFragment mSettingsFragment;
    SendFragment mSendFragment;
    OKFragment mOKFragment;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mLoadFragment = new LoadFragment();
        mLoadFragment.mActivity = this;
        mSettingsFragment = new SettingsFragment();
        mSendFragment = new SendFragment();
        mSendFragment.mMListener = this;
        mOKFragment = new OKFragment();
        if (savedInstanceState==null) {
            getSupportFragmentManager().beginTransaction()
                    .replace(R.id.frame, mLoadFragment)
                    .commit();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()) {
            case R.id.settingsButton:
                openSettings();
                return true;
            case android.R.id.home:
                getSupportFragmentManager().popBackStack();
                openOptionsMenu();
                getSupportActionBar().setTitle(R.string.app_name);
                getSupportActionBar().setHomeButtonEnabled(false);
                getSupportActionBar().setDisplayHomeAsUpEnabled(false);
                return true;
        }
        return false;
    }

    void openSettings(){
        if (getSupportFragmentManager().findFragmentById(R.id.frame)!=mSettingsFragment)
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.frame, mSettingsFragment)
                .addToBackStack(null)
                .commit();

    }

    @Override
    public void send(String s) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.frame, mSendFragment)
                .addToBackStack(null).commit();
    }

    @Override
    public void ok() {
        getSupportFragmentManager().popBackStack();
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.frame, mOKFragment)
                .addToBackStack(null).commit();
    }
}
