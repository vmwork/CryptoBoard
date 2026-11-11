<script setup lang="ts">
import {
    IconListTree,
    IconChartBar,
    IconDashboard,
    IconDatabase,
    IconFileAi,
    IconDeviceAnalytics,
    IconNfc,
    IconHelp,
    IconBrandBinance,
    IconBrandMessenger,
    IconCashRegister,
    IconSearch,
    IconSettings,
    IconUsers,
    IconMail,
} from "@tabler/icons-vue"

import NavDocuments from "@/components/NavDocuments.vue"
import NavMain from "@/components/NavMain.vue"
import NavSecondary from "@/components/NavSecondary.vue"
import NavUser from "@/components/NavUser.vue"
import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"

const data = {
    user: {
        name: "shadcn",
        email: "m@example.com",
        avatar: "/avatars/shadcn.jpg",
    },
    navMain: [
        {
            title: "Analytics",
            url: "#",
            icon: IconDeviceAnalytics,
        },
        {
            title: "Messages",
            url: "#",
            icon: IconMail,
            iconAfter: IconBrandMessenger,
        },
        {
            title: "Classifieds",
            url: "#",
            icon: IconListTree,
        },
        {
            title: "Transactions",
            url: "#",
            icon: IconCashRegister,
        },
        {
            title: "My NFTs",
            url: "#",
            icon: IconNfc,
        },
    ],

    navSecondary: [
        {
            title: "Settings",
            url: "#",
            icon: IconSettings,
        },
        {
            title: "Get Help",
            url: "#",
            icon: IconHelp,
        },
        {
            title: "Search",
            url: "#",
            icon: IconSearch,
        },
    ],
    documents: [
        {
            name: "Data Library",
            url: "#",
            icon: IconDatabase,
        },
    ],
}
</script>

<template>
    <Sidebar collapsible="offcanvas">
        <SidebarHeader>
            <SidebarMenu>
                <SidebarMenuItem>
                    <SidebarMenuButton as-child class="data-[slot=sidebar-menu-button]:!p-1.5">
                        <a href="/">
                            <svg width="180" height="36" viewBox="0 0 180 36" fill="none"
                                xmlns="http://www.w3.org/2000/svg" class="h-7 w-auto text-sidebar-foreground">
                                <!-- Иконка -->
                                <g transform="translate(0, 2)">
                                    <path d="M14 2L4 5.5V10.5C4 15.5 7.5 20.5 14 22C20.5 20.5 24 15.5 24 10.5V5.5L14 2Z"
                                        stroke="#00DC82" stroke-width="2" stroke-linejoin="round" />
                                    <path d="M9.5 12L12 14.5L18 9" stroke="#00DC82" stroke-width="2.5"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                </g>

                                <!-- Текст с currentColor -->
                                <text x="32" y="25" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="18"
                                    font-weight="700" fill="currentColor" letter-spacing="0">Crypto</text>
                                <text x="108" y="25" font-family="'Inter', 'Segoe UI', Arial, sans-serif" font-size="18"
                                    font-weight="700" fill="#00DC82" letter-spacing="0">Board</text>
                            </svg>
                        </a>
                    </SidebarMenuButton>
                </SidebarMenuItem>
            </SidebarMenu>
        </SidebarHeader>
        <SidebarContent>
            <NavMain :items="data.navMain" />
            <NavDocuments :items="data.documents" />
            <NavSecondary :items="data.navSecondary" class="mt-auto" />
        </SidebarContent>
        <SidebarFooter>
            <NavUser :user="data.user" />
        </SidebarFooter>
    </Sidebar>
</template>
