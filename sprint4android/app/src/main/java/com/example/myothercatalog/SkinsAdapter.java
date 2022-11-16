package com.example.myothercatalog;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class SkinsAdapter extends RecyclerView.Adapter<SkinViewHolder> {
    private SkinsList skins;

    public SkinsAdapter(SkinsList skins) {
        this.skins=skins;
    }

    @NonNull
    @Override
    public SkinViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.skin_recycler_cell, parent, false);
        SkinViewHolder viewHolder = new SkinViewHolder(view);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull SkinViewHolder holder, int position) {
        Skin data = this.skins.getSkins().get(position);
        holder.ShowData(data);
    }

    @Override
    public int getItemCount() {
        int items = this.skins.getSkins().size();
        return items;
    }
}
